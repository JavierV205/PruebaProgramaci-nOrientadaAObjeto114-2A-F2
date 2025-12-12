from clase.producto import Producto

class ProductoFisico(Producto):
    def __init__(self, codigo, nombre, precio, stock, categoria_envio):
        super().__init__(codigo, nombre, precio, stock)
        self.categoria_envio = categoria_envio

    def costo_envio(self):
        if self.categoria_envio == "liviano":
            return 1500
        elif self.categoria_envio == "estandar":
            return 3000
        else:
            return 6000

    def costo_total(self, cantidad):
        self.validar_cantidad(cantidad)
        return (self.precio * cantidad) + self.costo_envio()