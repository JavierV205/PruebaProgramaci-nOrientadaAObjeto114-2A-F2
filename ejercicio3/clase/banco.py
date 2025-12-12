class Banco:
    def __init__(self):
        self.cuentas = {}

    def agregar_cuenta(self, cuenta):
        if cuenta.numero_cuenta in self.cuentas:
            print("ERROR: Ya existe una cuenta con ese número.")
            return
        self.cuentas[cuenta.numero_cuenta] = cuenta

    def buscar_cuenta(self, numero_cuenta):
        return self.cuentas.get(numero_cuenta)

    def saldo_total(self):
        return sum(c.saldo for c in self.cuentas.values())
