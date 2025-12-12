class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.__codigo = codigo
        self.nombre = nombre
        self.__precio = precio
        self.stock = stock

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if codigo <= 0:
            raise Exception("EL CÓDIGO DEBE SER MAYOR A 0.")
        self.__codigo = codigo

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        if precio <= 0:
            raise Exception("EL PRECIO DEBE SER MAYOR QUE 0.")
        self.__precio = precio

    def costo_total(self, cantidad):
        raise Exception("Este método debe implementarse en las subclases.")

    def validar_cantidad(self, cantidad):
        if cantidad <= 0:
            raise Exception("La cantidad debe ser mayor a cero.")
        if cantidad > self.stock:
            raise Exception("No hay stock suficiente disponible.")


