class Motocicleta():
    def __init__(self, matricula, tarifacion: 0.08):
        self.matricula = matricula
        self.tarifacion = tarifacion

    @property
    def matricula(self):
        return self.matricula

    def matricula(self,matricula):
        self.matricula = matricula

    @property
    def tarifacion(self):
        return self.tarifacion

    def tarifacion(self, tarifacion):
        self.tarifacion = tarifacion
