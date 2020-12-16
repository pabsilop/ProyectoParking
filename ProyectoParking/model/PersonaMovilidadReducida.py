class PersonaMovilidadReducida():
    def __init__(self, tarifacion:0.10):
        self.tarifacion = tarifacion

    @property
    def tarifacion(self):
        return self.tarifacion

    def tarifacion(self, tarifacion):
        self.tarifacion = tarifacion


