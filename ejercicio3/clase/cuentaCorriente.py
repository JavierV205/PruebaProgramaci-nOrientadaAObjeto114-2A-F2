from clase.cuentas import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, numero_cuenta, nombre, saldo_inicial=0, linea_credito=0):
        super().__init__(numero_cuenta, nombre, saldo_inicial)
        self.__linea_credito = linea_credito

    @property
    def linea_credito(self):
        return self.__linea_credito

    def retirar(self, monto):
        if monto <= 0:
            raise Exception("El retiro debe ser mayor a cero.")

        if self.saldo - monto < -self.linea_credito:
            raise Exception("Saldo insuficiente, excede la línea de crédito.")

        self.saldo -= monto
        self.movimientos.append(f"RETIRO: {monto:.2f}")