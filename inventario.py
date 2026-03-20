import csv
import requests
from dataclasses import dataclass, field


@dataclass
class Producto:
    nombre: str
    precio: float
    categoria: str
    stock: int = field(default=0)

    def aplicar_descuento(self, porcentaje: float) -> float:
        self.precio = self.precio * (1 - porcentaje / 100)
        return self.precio


def cargar_productos(ruta: str) -> list[Producto]:
    productos: list[Producto] = []

    with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo, skipinitialspace=True)
        for fila in lector:
            producto = Producto(
                nombre=fila["nombre"],
                precio=float(fila["precio"]),
                categoria=fila["categoria"],
                stock=int(fila["stock"]),
            )
            productos.append(producto)

    return productos

def filtrar_por_categoria(productos: list[Producto], categoria: str) -> list[Producto]:
    return [producto for producto in productos if producto.categoria == categoria]


def obtener_tipo_cambio() -> float:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    respuesta = requests.get(url)
    datos = respuesta.json()
    tipo_cambio = datos["rates"]["MXN"]
    return tipo_cambio


def main():
    productos = cargar_productos("productos.csv")
    
    tipo_cambio = obtener_tipo_cambio()
    print(f"Tipo de cambio USD/MXN: {tipo_cambio}\n")
    
    categoria_filtro = "Electronica"
    productos_filtrados = filtrar_por_categoria(productos, categoria_filtro)
    
    print(f"Productos en categoría '{categoria_filtro}':")
    for producto in productos_filtrados:
        precio_mxn = producto.precio * tipo_cambio
        print(f"  {producto.nombre}: ${producto.precio} USD = ${precio_mxn:.2f} MXN")


if __name__ == "__main__":
    main()