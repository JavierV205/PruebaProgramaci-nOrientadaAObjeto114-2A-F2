# Ejercicio 3 — Cuentas bancarias, movimientos y reporte
# Un banco necesita un sistema para administrar las cuentas de sus clientes, registrar los movimientos
# que se realizan y generar reportes de saldos e historial.
# Como usuario del sistema, se requiere que éste permita:
# 1. Registrar cuentas bancarias de clientes, almacenando al menos:
# • Número de cuenta.
# • Nombre del titular.
# • Saldo actual.
# • Tipo de cuenta (por ejemplo: cuenta corriente, cuenta de ahorro).
# 2. Registrar distintos tipos de cuentas, donde:
# • Las cuentas corrientes puedan operar con línea de crédito, es decir, permitir que el saldo
# baje de cero hasta cierto límite negativo.
# • Las cuentas de ahorro puedan tener asociada una tasa de interés mensual, que permita
# actualizar el saldo aplicando dicho interés.
# 3. Registrar y controlar movimientos de dinero en una cuenta, específicamente:
# • Depósitos, que aumenten el saldo, rechazando montos no válidos (cero o negativos).
# • Retiros, que disminuyan el saldo:
# o En cuentas normales o de ahorro, solo si hay saldo suficiente.
# o En cuentas corrientes, permitiendo sobregiro hasta el límite de la línea de crédito.
# • Cada movimiento debe quedar registrado como un texto legible (por ejemplo, “DEPÓSITO
# 100.000”, “RETIRO 50.000”, “INTERÉS 2.500”).
# 4. Aplicar intereses a las cuentas de ahorro, de forma que:
# • Dado un periodo mensual, el sistema pueda calcular el interés correspondiente según la
# tasa definida para esa cuenta.
# • El saldo se actualice sumando el interés calculado.
# • El interés aplicado quede igualmente registrado como un movimiento.
# 5. Consultar la información de una cuenta bancaria, permitiendo:
# • Buscar una cuenta por su número.
# • Ver el titular, el tipo de cuenta y su saldo actual.
# • Obtener el historial de movimientos realizados en esa cuenta, en orden cronológico.
# 6. Administrar el conjunto de cuentas del banco, pudiendo:
# • Agregar nuevas cuentas.
# • Consultar si una cuenta existe a partir de su número.
# • Obtener el saldo total administrado por el banco, sumando el saldo de todas las cuentas
# registradas.
# 7. Probar el sistema desde un programa principal, donde se simule:
# • La creación de varias cuentas de distintos tipos (por ejemplo, dos cuentas corrientes y dos
# cuentas de ahorro).
# • La ejecución de depósitos y retiros en distintas cuentas.
# • La aplicación de intereses en al menos una cuenta de ahorro.
# • La impresión de:
# o El saldo y tipo de cada cuenta.
# o El historial de movimientos de una cuenta específica.
# o El saldo total administrado por el banco.



from clase.cuentaCorriente import CuentaCorriente
from clase.cuentaAhorro import CuentaAhorro
from clase.banco import Banco


def main():
    banco = Banco()

    cc1 = CuentaCorriente("1001", "Ana Pérez", 1000, 500)
    cc2 = CuentaCorriente("1002", "Luis Gómez", 500, 1000)
    ca1 = CuentaAhorro("2001", "Juan Soto", 2000, 2.0)
    ca2 = CuentaAhorro("2002", "Maria Ruiz", 3000, 1.5)

    banco.agregar_cuenta(cc1)
    banco.agregar_cuenta(cc2)
    banco.agregar_cuenta(ca1)
    banco.agregar_cuenta(ca2)

    cc1.depositar(500)
    cc2.retirar(800)
    ca1.retirar(1000)
    ca1.aplicar_interes()

    print("=== Saldo y tipo de cada cuenta ===")
    for cuenta in banco.cuentas.values():
        print(cuenta.obtener_informacion())

    print("\n=== Historial de la cuenta 2001 ===")
    cuenta = banco.buscar_cuenta("2001")
    print(cuenta.mostrar_historial())

    print("\nSaldo total del banco:", banco.saldo_total())


if __name__ == "__main__":
    main()