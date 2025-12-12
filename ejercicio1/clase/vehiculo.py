class Vehiculo:
    def __init__(self,codigo_motor,modelo,marca,año_fabricacion):
        self.__codigo_motor=codigo_motor
        self.modelo=modelo
        self.marca=marca
        self.año_fabricacion=año_fabricacion

    @property
    def codigo_motor(self):
        return self.__codigo_motor
    
    @codigo_motor.setter
    def codigo_motor(self,codigo_motor):
        if codigo_motor<100:
            raise Exception("EL CODIGO DE MOTOR DEBE SER MAYOR A 100")
        self.__codigo_motor=codigo_motor

    def descripcion(self):
        return (f"motor: {self.codigo_motor}. Modelo: {self.modelo}. Marca: {self.marca}. año de fabricacion:{self.año_fabricacion}")

    def consumo_de_combustible(self,km):
        raise Exception("EL METODO SE DEBE INCLUIR EN LAS SUBCLASES.")