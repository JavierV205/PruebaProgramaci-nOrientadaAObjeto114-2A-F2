from clase.trabajadores import Trabajador

class Practicante(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, horas_trabajadas, valor_hora, activo=True):
        super().__init__(nombre, rut, sueldo_base, activo)
        self.horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora

    @property
    def valor_hora(self):
        return self.__valor_hora

    def remuneracion_mensual(self):
        return self.horas_trabajadas * self.valor_hora
    