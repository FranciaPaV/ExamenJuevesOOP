class Shots:
    def __init__(self):
        self.nombre = None
        self.precio = None
        self.gradosalcohol = None
        self.temperatura = None
        
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
    def gradosalcohol(self):
        return self.__gradosalcohol
    
    @gradosalcohol.setter
    def gradosalcohol(self, dato):
        self.__gradosalcohol = dato
        
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, dato):
        self.__temperatura = dato
    