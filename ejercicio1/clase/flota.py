class FlotaVehiculos:
    def __init__(self):
        self.vehiculos = {}

    def agregar_vehiculo(self, vehiculo):
        if vehiculo.codigo_motor in self.vehiculos:
            print("ERROR: Ya existe un vehículo con ese código de motor.")
            return
        self.vehiculos[vehiculo.codigo_motor] = vehiculo

    def eliminar_vehiculo(self, codigo_motor):
        self.vehiculos.pop(codigo_motor, None)

    def buscar_vehiculo(self, codigo_motor):
        return self.vehiculos.get(codigo_motor)

    def listar_vehiculos(self):
        return list(self.vehiculos.values())

    def consumo_total(self, km):
        total = 0
        for vehiculo in self.vehiculos.values():
            total += vehiculo.consumo_de_combustible(km)
        return total