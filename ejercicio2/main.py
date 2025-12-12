# Ejercicio 2 — Gestión de empleados, bonos y reportes de sueldo
# Una empresa quiere contar con un sistema para administrar a sus trabajadores y estimar el gasto
# mensual en sueldos, considerando que existen distintos tipos de colaboradores con formas
# diferentes de cálculo de remuneración.
# Se requiere que éste permita:
# 1. Registrar trabajadores de la empresa, almacenando como mínimo:
# • Nombre completo.
# • Identificación (por ejemplo, RUT).
# • Sueldo base.
# • Estado del trabajador (activo o inactivo).
# 2. Manejar distintos tipos de trabajadores, tales como por ejemplo:
# • Vendedores.
# • Gerentes.
# • Practicantes (o trabajadores a honorarios por hora).
# Cada tipo de trabajador debe considerar información adicional propia de su rol (por ejemplo:
# comisiones, bonos, horas trabajadas, etc.) y esa información debe afectar la forma en que se calcula
# su remuneración final.
# 3. Calcular la remuneración mensual final de cada trabajador, de manera que:
# • Exista un cálculo base a partir del sueldo asignado.
# • Para quienes reciben comisiones (como los vendedores), la remuneración final considere
# las ventas del mes y el porcentaje de comisión.
# • Para quienes reciben bonos fijos (como los gerentes), la remuneración final incorpore dicho
# bono al sueldo base.
# • Para quienes trabajan por hora (como practicantes), la remuneración se calcule según
# cantidad de horas trabajadas y valor por hora.
# 4. Obtener un resumen legible de cada trabajador, donde se pueda ver, al menos:
# • Nombre.
# • Identificación.
# • Tipo de trabajador.
# • Sueldo base.
# • Remuneración final calculada para el mes.
# 5. Administrar el conjunto de trabajadores de la empresa, pudiendo:
# • Agregar nuevos trabajadores indicando su tipo y la información asociada.
# • Mantener un listado de todos los trabajadores.
# • Filtrar o listar solamente los trabajadores activos (es decir, aquellos que deben considerarse
# para el cálculo de sueldos del mes).
# 6. Calcular indicadores globales de la empresa, en particular:
# • El gasto total mensual en sueldos, considerando únicamente a los trabajadores activos.
# • (Opcional) Un listado donde se puedan comparar las remuneraciones finales por trabajador
# para identificar quiénes representan mayor o menor costo mensual.
# 7. Probar el sistema desde un programa principal, donde se simule:
# • La creación de varios trabajadores de distintos tipos (vendedores, gerentes, practicantes)
# con datos de ejemplo.
# • Su incorporación al conjunto de trabajadores de la empresa.
# • La obtención de un reporte que muestre:
# o Nombre, tipo de trabajador y remuneración final de cada uno.
# o El gasto total mensual de la empresa en sueldos.

from clase.vendedor import Vendedor
from clase.gerente import Gerente
from clase.practicante import Practicante
from clase.empresa import Empresa

def main():
    empresa = Empresa()

    # Crear trabajadores de ejemplo
    v1 = Vendedor("Ana Pérez", "11111111-1", 500000, ventas_mes=2000000, porcentaje_comision=0.05)
    g1 = Gerente("Luis Gómez", "22222222-2", 1500000, bono_fijo=300000)
    p1 = Practicante("Juan Soto", "33333333-3", 0, horas_trabajadas=120, valor_hora=5000)

    # Agregarlos a la empresa
    empresa.agregar_trabajador(v1)
    empresa.agregar_trabajador(g1)
    empresa.agregar_trabajador(p1)

    # Mostrar reporte
    print("=== Reporte de trabajadores ===")
    for t in empresa.listar_trabajadores():
        print(t.descripcion())

    # Gasto total mensual
    print("\nGasto total mensual (trabajadores activos):", empresa.gasto_total_mensual())

if __name__ == "__main__":
    main()