#TDA Pila

import numpy as np

class Pila:
    def __init__(self, capacidad, tipo):
        self.pila = np.zeros(shape=(capacidad), dtype = tipo)
        self.cima = None
        
    def toEmpty(self):
        self.cima = None
        
    def push(self, dato):
        if self.isEmpty(): self.cima = -1
        if not self.isFull():
            self.pila[self.cima + 1] = dato
            self.cima += 1
        else:
            raise Exception("Está llena")
            
    def pop(self):
        cimaAux = self.cima
        if not self.isEmpty():
            self.cima -= 1
        else:
            raise Exception("Está vacía")
        if self.cima == -1:
           self.cima = None 
        return cimaAux
    
    def top(self):
        return self.pila[self.cima]
    
    def toClone(self):
        nueva = Pila(len(self.pila), self.pila.dtype)
        if not self.isEmpty():
            for i in range(self.cima+1):
                nueva.pila[i] = self.pila[i]
            nueva.cima = self.cima
        return nueva        
        
    def size(self):
        if self.isEmpty(): self.cima = -1
        return self.cima +1
        
    def isEmpty(self):
        return self.cima == None
        
    def isFull(self):
        return self.cima == len(self.pila)-1
    
    def printStack(self):
        for i in range(len(self.pila)):
            print( self.pila[i], end = ' ')
            
    def length(self):
        return len(self.pila)
        
    
    
    
    
    
        
        
