class Cuenta:
    def __init__(self, numero_cuenta, nombre, saldo_inicial=0):
        self.__numero_cuenta = numero_cuenta
        self.nombre = nombre
        self.__saldo = saldo_inicial
        self.movimientos = []

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    def depositar(self, monto):
        if monto <= 0:
            raise Exception("EL DEPÓSITO DEBE SER MAYOR A 0.")
        self.saldo += monto
        self.movimientos.append(f"DEPÓSITO: {monto:.2f}")

    def retirar(self, monto):
        raise Exception("Este método debe implementarse en subclases.")

    def obtener_informacion(self):
        return (f"Cuenta: {self.numero_cuenta} | Titular: {self.nombre} | "
                f"Tipo: {self.__class__.__name__} | Saldo: {self.saldo:.2f}")

    def mostrar_historial(self):
        return "\n".join(self.movimientos)