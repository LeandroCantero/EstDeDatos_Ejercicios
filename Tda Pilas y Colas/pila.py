#TDA Pila

import numpy as np

class Pila:
    def __init__(self, capacidad, tipo = int):
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
        if self.cima == 0:
           self.cima = None 
        elif not self.isEmpty():
            self.cima -= 1
        else:
            raise Exception("Está vacía")
    
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
        return self.cima +1
        
    def isEmpty(self):
        return self.cima == None
        
    def isFull(self):
        return self.cima == self.capacidad-1
    
    def printStack(self):
        return self.pila
        
    
    
    
    
    
        
        
