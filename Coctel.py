class Coctel:
    def __init__(self):
        self.nombre = None
        self.precio = None
        self.cantidadAlcohol = None
        self.diasHecho = None
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, dato):
        self.nombre = dato
    
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, dato):
        self.precio = dato
    
    @property
    def cantidadAlcohol(self):
        return self._cantidadAlcohol
    @cantidadAlcohol.setter
    def cantidadAlcohol(self, dato):
        self.cantidadAlcohol = dato
    
    @property
    def diasHecho(self):
        return self._diasHecho
    @diasHecho.setter
    def diasHecho(self, dato):
    