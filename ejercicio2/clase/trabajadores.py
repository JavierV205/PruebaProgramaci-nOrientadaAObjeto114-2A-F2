class Trabajador:
    def __init__(self, nombre, rut, sueldo_base, activo=True):
        self.nombre = nombre
        self.__rut = rut
        self.__sueldo_base = sueldo_base
        self.activo = activo

    @property
    def rut(self):
        return self.__rut

    @property
    def sueldo_base(self):
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, sueldo_base):
        if sueldo_base < 0:
            raise Exception("EL SUELDO DEBE SER MAYOR A 0")
        self.__sueldo_base = sueldo_base

    def remuneracion_mensual(self):
        raise NotImplementedError("Este método debe implementarse en subclases.")

    def descripcion(self):
        return (f"Nombre: {self.nombre} | ID: {self.rut} | "
                f"Tipo: {self.__class__.__name__} | Sueldo Base: {self.sueldo_base:.2f} | "
                f"Remuneración Final: {self.remuneracion_mensual():.2f}")