import csv
import requests
from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    category: str
    stock: int = field(default=0)

    def apply_discount(self, percentage: float) -> float:
        self.price = self.price * (1 - percentage / 100)
        return self.price


def load_products(path: str) -> list[Product]:
    products: list[Product] = []

    with open(path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for row in reader:
            product = Product(
                name=row["name"],
                price=float(row["price"]),
                category=row["category"],
                stock=int(row["stock"]),
            )
            products.append(product)

    return products


def filter_by_category(products: list[Product], category: str) -> list[Product]:
    return [product for product in products if product.category == category]


def get_exchange_rate() -> float:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"]["MXN"]
    return exchange_rate


def main():
    products = load_products("products.csv")

    exchange_rate = get_exchange_rate()
    print(f"USD/MXN exchange rate: {exchange_rate}\n")

    category_filter = "Electronics"
    filtered_products = filter_by_category(products, category_filter)

    print(f"Products in category '{category_filter}':")
    for product in filtered_products:
        price_mxn = product.price * exchange_rate
        print(f"  {product.name}: ${product.price} USD = ${price_mxn:.2f} MXN")


if __name__ == "__main__":
    main()
