class Plaza():
    def __init__(self, id, tipoVehiculo):
        self.id = id
        self.tipoVehiculo = tipoVehiculo

    @property
    def id(self):
        return self.id

    def id(self,id):
        self.id == id

    @property
    def tipoVehiculo(self):
        return self.tipoVehiculo

    def tipoVehiculo(self, tipoVehiculo):
        self.tipoVehiculo = tipoVehiculo

