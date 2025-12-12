from clase.vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self,codigo_motor,modelo,marca,año_fabricacion,capacidad_carga):
        super().__init__(codigo_motor, modelo, marca, año_fabricacion)
        self.capacidad_carga=capacidad_carga #Ejemplo en toneladas


    def consumo_de_combustible(self, km):
        #eficiencia base 5 km/l, peor mientras más carga.
        eficiencia=5 - (self.capacidad_carga*0.2)
        if eficiencia<2:
            eficiencia=2 #es el limite.
        return km / eficiencia