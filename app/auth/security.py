from datetime import datetime, timedelta, timezone
import os
from typing import Any
from dotenv import load_dotenv
from jose import JWTError, jwt
from passlib.context import CryptContext

load_dotenv()

def _get_secret_key() -> str:
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        raise RuntimeError("SECRET_KEY is not set")
    return secret_key

SECRET_KEY = _get_secret_key()
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(
    data: dict[str, Any], expires_delta: timedelta | None = None
) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str) -> dict[str, Any] | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
