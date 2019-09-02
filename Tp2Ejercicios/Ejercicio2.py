'''
Diseñar el TDA fraccion, para representar numeros fraccionarios. Implementar las
siguientes operaciones: Crear, obtener numerador, obtener denominador, modificar
numerador, modificar denominador, sumar, restar, multiplicar, dividir, simplificar e
iguales (recibe dos fracciones e informa si son iguales o distintas).
'''

class Fraccion:
    def __init__(self, num = 0, den = 0):
        self.numerador = num
        self.denominador = den
        
    def crear(n, d):
        self.numerador = n
        self.denominador = d
        
    def getNumerador():
        return self.numerador

    def getDenominador():
        return self.denominador
    
    def modNumerador(n):
        self.numerador = n
        
    def modDenominador(d):
        self.denominador = d
        
    def sumar(self, fraccion2):
        if self.denominador == fraccion2.denominador:
            self.numerador + fraccion2.numerador
        else:
            
        
        
        


