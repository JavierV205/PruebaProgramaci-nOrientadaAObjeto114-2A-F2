# Ejercicio 4 — Productos, venta online y carrito de compras
# Una tienda online necesita un sistema para gestionar sus productos y permitir a los clientes armar
# un carrito de compras que considere las particularidades de cada tipo de producto.
# Se requiere que éste permita:
# 1. Registrar productos disponibles para la venta, almacenando al menos:
# • Código o identificador del producto.
# • Nombre.
# • Precio unitario.
# • Stock disponible (cantidad en bodega).
# 2. Trabajar con diferentes tipos de productos, distinguiendo, como mínimo, entre:
# • Productos físicos (por ejemplo: libros, ropa, accesorios).
# • Productos digitales (por ejemplo: cursos online, licencias de software, archivos
# descargables).
# Cada tipo de producto debe considerar información adicional propia (como peso para los físicos,
# tamaño de descarga o tipo de licencia para los digitales) y esa información debe influir en el cálculo
# del valor final.
# 3. Calcular el costo total de un producto para una cantidad solicitada, de manera que:
# • Se valide que la cantidad pedida sea positiva y no exceda el stock disponible.
# • Para productos físicos se pueda considerar un costo de envío adicional, que puede variar
# según una categoría de envío (por ejemplo: “liviano”, “estándar”, “pesado”).
# • Para productos digitales se pueda considerar, si corresponde, un recargo asociado a la
# licencia, como una tarifa adicional para licencias comerciales.
# 4. Mantener actualizado el stock de los productos, de modo que:
# • Al agregar un producto al carrito se verifique que existe stock suficiente.
# • Tras una compra (o simulación de compra), el stock se vea reflejado correctamente,
# evitando vender más unidades de las disponibles.
# 5. Administrar un carrito de compras, con la posibilidad de:
# • Agregar productos indicando la cantidad deseada.
# • Eliminar productos del carrito a partir de su código o identificador.
# • Ver el detalle de los ítems agregados, mostrando para cada uno:
# o Nombre del producto.
# o Tipo de producto (físico o digital).
# o Cantidad.
# o Total calculado para ese producto (considerando envío o recargos, según
# corresponda).
# 6. Obtener el total general del carrito, es decir:
# • El monto total a pagar sumando todos los productos agregados con sus respectivos costos
# adicionales (envío, recargos, etc.).
# • (Opcional) Mostrar también el subtotal sin recargos y el monto total de recargos aplicados.
# 7. Probar el sistema desde un programa principal, donde se simule:
# • La creación de varios productos físicos y digitales con datos de ejemplo.
# • La incorporación de algunos de ellos al carrito con distintas cantidades.
# • La visualización del detalle de los ítems del carrito.
# • El cálculo e impresión del total final a pagar por la “compra”.
from clase.productoDigital  import ProductoDigital
from clase.productoFisico  import ProductoFisico
from clase.carrito  import Carrito

def main():
    # Crear productos
    p1 = ProductoFisico("A001", "Libro Programación", 15000, 20, "liviano")
    p2 = ProductoFisico("A002", "Polera Deportiva", 12000, 15, "estandar")
    p3 = ProductoDigital("D101", "Curso Python", 25000, 100, "personal")
    p4 = ProductoDigital("D102", "Software Pro", 40000, 50, "comercial")

    carrito = Carrito()

    # Agregar productos al carrito
    carrito.agregar_producto(p1, 2)
    carrito.agregar_producto(p3, 1)
    carrito.agregar_producto(p4, 1)

    # Mostrar detalle
    print("=== Detalle del carrito ===")
    print(carrito.detalle())

    # Total general
    print("\nTotal a pagar:", carrito.total_general())

    # Mostrar stock actualizado
    print("\n=== Stock actualizado ===")
    print(f"{p1.nombre}: {p1.stock}")
    print(f"{p3.nombre}: {p3.stock}")
    print(f"{p4.nombre}: {p4.stock}")


if __name__ == "__main__":
    main()
