class Coctel:
    def __init__(self):
        self.nombre = None
        self.precio = None
        self.cantidadAlcohol = None
        self.diasHecho = None
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato
    
    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, dato):
        self.__precio = dato
    
    @property
    def cantidadAlcohol(self):
        return self.__cantidadAlcohol
    @cantidadAlcohol.setter
    def cantidadAlcohol(self, dato):
        self.__cantidadAlcohol = dato
    
    @property
    def diasHecho(self):
        return self.__diasHecho
    @diasHecho.setter
    def diasHecho(self, dato):
        self.__diasHecho = dato
    