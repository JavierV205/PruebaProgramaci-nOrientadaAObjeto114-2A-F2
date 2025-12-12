from clase.trabajadores import Trabajador

class Gerente(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, bono_fijo, activo=True):
        super().__init__(nombre, rut, sueldo_base, activo)
        self.__bono_fijo = bono_fijo

    @property
    def bono_fijo(self):
        return self.__bono_fijo

    def remuneracion_mensual(self):
        return self.sueldo_base + self.bono_fijo