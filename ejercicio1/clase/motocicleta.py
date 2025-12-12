from clase.vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self,codigo_motor,modelo,marca,año_fabricacion,cilindrada):
        super().__init__(codigo_motor, modelo, marca, año_fabricacion)
        self.cilindrada=cilindrada


    # motos pequeñas gastan poco, motos grandes gastan más
    def consumo_de_combustible(self, km):
        if self.cilindrada <=150:
            eficiencia=35
        elif self.cilindrada <=300:
            eficiencia=28
        else:
            eficiencia=20
        return km / eficiencia