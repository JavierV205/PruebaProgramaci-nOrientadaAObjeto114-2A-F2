from clase.vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self,codigo_motor,modelo,marca,año_fabricacion,puertas):
        super().__init__(codigo_motor, modelo, marca, año_fabricacion)
        self.puertas=puertas
    

    
    # consumo base: 12 km/l, autos con más puertas gastan un poco más
    def consumo_de_combustible(self, km):
        eficiencia=12-(self.puertas - 2) *0.5
        return km / eficiencia
