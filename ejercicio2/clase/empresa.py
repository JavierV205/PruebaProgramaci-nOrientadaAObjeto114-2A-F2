class Empresa:
    def __init__(self):
        self.trabajadores = {}  # diccionario: rut -> trabajador

    def agregar_trabajador(self, trabajador):
        if trabajador.rut in self.trabajadores:
            print("ERROR: YA EXISTE UN TRABAJADOR CON ESTE RUT")
            return
        self.trabajadores[trabajador.rut] = trabajador

    def listar_trabajadores(self):
        return list(self.trabajadores.values())

    def listar_activos(self):
        return [t for t in self.trabajadores.values() if t.activo]

    def gasto_total_mensual(self):
        total = 0
        for trabajador in self.listar_activos():
            total += trabajador.remuneracion_mensual()
        return total
