#TDA Cola

import numpy as np

class Cola:
    def __init__(self, capacidad, tipo = int):
        self.cola = np.zeros(shape=(capacidad), dtype = tipo)
        self.fin = None
        
    def toEmpty(self):
        self.fin = None
        
    def queue(self, dato):
        if self.isEmpty(): self.fin = -1
        if not self.isFull():
            self.cola[self.fin +1] = dato
            self.fin += 1
        else:
            raise Exception("Está llena")
            
    def dequeue(self):
        if self.fin == -1:
            self.fin = None
        if not self.isEmpty():
            for i in range(self.fin):
                self.cola[i] = self.cola[i+1]
            self.cola[self.fin+1] = 0
            self.fin -= 1
        else:
            raise Exception("Está vacía")
    
    def top(self):
        return self.cola[self.fin]
    
    def toClone(self):
        nueva = Cola(len(self.cola, self.cola.dtype))
        if not self.isEmpty():
            for i in range(self.fin +1):
                   nueva.cola[i] = self.cola[i]
            nueva.fin = self.fin
        return nueva
    
    def size(self):
        return self.fin +1
    
    def isEmpty(self):
        return self.fin == None
    
    def isFull(self):
        return self.fin == self.capacidad-1
    
    def printQueue(self):
        for i in range(len(self.cola)):
            print(self.cola[i], end = ' ')
            
        
