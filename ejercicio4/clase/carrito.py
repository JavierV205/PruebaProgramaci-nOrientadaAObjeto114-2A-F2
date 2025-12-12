class Carrito:
    def __init__(self):
        self.items = {}

    def agregar_producto(self, producto, cantidad):
        producto.validar_cantidad(cantidad)

        if producto.codigo in self.items:
            self.items[producto.codigo][1] += cantidad
        else:
            self.items[producto.codigo] = [producto, cantidad]

        producto.stock -= cantidad

    def eliminar_producto(self, codigo):
        if codigo in self.items:
            producto, cantidad = self.items[codigo]
            producto.stock += cantidad  # devolver stock
            del self.items[codigo]

    def detalle(self):
        lineas = []
        for producto, cantidad in self.items.values():
            total = producto.costo_total(cantidad)
            tipo = producto.__class__.__name__
            lineas.append(
                f"{producto.nombre} | Tipo: {tipo} | Cant: {cantidad} | Total: ${total}"
            )
        return "\n".join(lineas)

    def total_general(self):
        total = 0
        for producto, cantidad in self.items.values():
            total += producto.costo_total(cantidad)
        return total