from clase.trabajadores import Trabajador

class Vendedor(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, ventas_mes, porcentaje_comision, activo=True):
        super().__init__(nombre, rut, sueldo_base, activo)
        self.__ventas_mes = ventas_mes
        self.__porcentaje_comision = porcentaje_comision

    @property
    def ventas_mes(self):
        return self.__ventas_mes

    @property
    def porcentaje_comision(self):
        return self.__porcentaje_comision

    def remuneracion_mensual(self):
        return self.sueldo_base + self.ventas_mes * self.porcentaje_comision