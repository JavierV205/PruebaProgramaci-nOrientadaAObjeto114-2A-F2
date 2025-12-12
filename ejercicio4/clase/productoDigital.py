from clase.producto import Producto

class ProductoDigital(Producto):
    def __init__(self, codigo, nombre, precio, stock, tipo_licencia):
        super().__init__(codigo, nombre, precio, stock)
        self.tipo_licencia = tipo_licencia

    def recargo_licencia(self):
        if self.tipo_licencia == "comercial":
            return 5000
        return 0

    def costo_total(self, cantidad):
        self.validar_cantidad(cantidad)
        return (self.precio * cantidad) + self.recargo_licencia()