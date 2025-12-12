from clase.cuentas import Cuenta

class CuentaAhorro(Cuenta):
    def __init__(self, numero_cuenta, nombre, saldo_inicial=0, tasa_interes=0):
        super().__init__(numero_cuenta, nombre, saldo_inicial)
        self.tasa_interes = tasa_interes

    def retirar(self, monto):
        if monto <= 0:
            raise Exception("El retiro debe ser mayor a cero.")

        if monto > self.saldo:
            raise Exception("Saldo insuficiente.")

        self.saldo -= monto
        self.movimientos.append(f"RETIRO: {monto:.2f}")

    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes / 100
        self.saldo += interes
        self.movimientos.append(f"INTERÉS: {interes:.2f}")