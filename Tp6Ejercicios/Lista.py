#Lista

import NodoLista

class Lista:
    def __init__(self):
        self.primero = None
        
    def isEmpty(self):
        return self.primero == None
    
    def tamanio(self):
        contador = 0
        aux = self.primero
        while aux.siguiente != None:
            contador +=1
            aux = aux.siguiente
        return contador
    
    def vaciar(self):
        self.primero = None
        
    def obtenerElemento(self, pos):
        aux = self.primero          
        if pos == 0:
            aux = self.primero
        elif pos == 1:
            aux = aux.siguiente
        else:
            for i in range(pos-1):
                aux = aux.siguiente
        return aux
    
    def append(self, dato):
        nuevo = NodoLista(dato)
        if self.isEmpty():
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo
            
    def reemplazar(self, dato, pos):
        nuevo = NodoLista(dato)
        aux = self.primero
        for i in range(pos-1):
            aux = aux.siguiente
        if pos == self.tamanio():
            aux = nuevo
        else:
            aux2 = aux.siguiente
            aux = nuevo
            aux.siguiente = aux2
                        
    def eliminarElemento(self, pos):
        aux = self.primero
        if pos == 0:
            aux2 = aux.siguiente
            aux = None
            self.primero = aux2
        elif pos == 1:
            aux = aux.siguiente.siguiente
        else:
            for i in range(pos-1):
                aux = aux.siguiente
            aux = aux.siguiente.siguiente           
        
    #def instertarElementoEn(self, dato, pos):
        
    def imprimir(self):
        aux = self.primero
        while aux.siguiente != None:
            aux = aux.siguiente
            print(aux)     
        