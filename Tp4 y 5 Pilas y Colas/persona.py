#Tda Persona

class Persona:
    def __init__(self, nomb, ape, ed = 0):
        self.nombre = nomb
        self.apellido = ape
        self.edad = ed
    
    def getEdad(self):
        return self.edad
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    
    def setEdad(self, años):
        self.edad = años
    def setNombre(self, name):
        self.nombre = name
    def setApellido(self, surname):
        self.apellido = surname
