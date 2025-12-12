# E1 — Flota de Vehículos y Consumo de Combustible
# Una empresa de transporte quiere contar con un sistema para gestionar su flota de vehículos y
# estimar el consumo de combustible de cada uno, así como el consumo total para ciertos trayectos.
# Se necesita que éste permita:
# 1. Registrar vehículos de la flota, almacenando al menos:
# • Identificación del vehículo (por ejemplo, patente).
# • Marca.
# • Modelo.
# • Año de fabricación.
# 2. Trabajar con distintos tipos de vehículos dentro de la misma flota, por ejemplo:
# • Automóviles.
# • Motocicletas.
# • Camiones.
# Cada tipo de vehículo debe considerar información adicional relevante a su naturaleza (por
# ejemplo, cantidad de puertas, cilindrada, capacidad de carga, etc.), y esa información debe influir
# en cómo se estima su consumo de combustible.
# 3. Calcular el consumo estimado de combustible para un vehículo específico, dado un trayecto de
# cierta cantidad de kilómetros.
# • La forma de calcular el consumo no debe ser igual para todos, sino que debe poder
# diferenciar entre los distintos tipos de vehículo.
# 4. Obtener una descripción legible de cada vehículo, donde se pueda ver claramente:
# • Identificación (patente u otro identificador único).
# • Marca, modelo y año.
# • Tipo de vehículo.
# 5. Administrar la flota completa, pudiendo:
# • Agregar nuevos vehículos asegurando que no se repitan identificadores.
# • Eliminar vehículos a partir de su identificador.
# • Buscar un vehículo por su identificador para consultar sus datos y su consumo estimado.
# 6. Calcular indicadores globales de la flota, al menos:
# • Consumo total estimado de combustible para un trayecto de X kilómetros, considerando
# todos los vehículos registrados.
# • (Opcional) Listado de consumos individuales para comparar qué vehículos son más o
# menos eficientes.
# 7. Probar el sistema desde un programa principal, donde se simule lo siguiente:
# • Crear varios vehículos de distintos tipos con datos de ejemplo.
# • Agregarlos a la flota.
# • Mostrar la información de cada vehículo.
# • Calcular y mostrar el consumo estimado por vehículo y el consumo total de la flota para un
# trayecto común (por ejemplo, 150 km).
from clase.automovil import Automovil
from clase.camion import Camion
from clase.motocicleta import Motocicleta
from clase.flota import FlotaVehiculos


def main():
    flota = FlotaVehiculos()

    # Crear vehículos
    auto = Automovil(101, "Corolla", "Toyota", 2018, 4)
    moto = Motocicleta(202, "CBR", "Honda", 2020, 650)
    camion = Camion(303, "FH", "Volvo", 2015, 12)

    # Agregarlos a la flota
    flota.agregar_vehiculo(auto)
    flota.agregar_vehiculo(moto)
    flota.agregar_vehiculo(camion)

    # Mostrar descripción de cada vehículo
    print("\n=== Vehículos en la flota ===")
    for v in flota.listar_vehiculos():
        print(v.descripcion())

    # Consumo individual para 150 km
    km = 150
    print(f"\n=== Consumo por {km} km ===")
    for v in flota.listar_vehiculos():
        print(f"{v.codigo_motor}: {v.consumo_de_combustible(km):.2f} litros")

    # Consumo total
    print("\nConsumo total de la flota:", flota.consumo_total(km), "litros")

if __name__ == "__main__":
    main()
