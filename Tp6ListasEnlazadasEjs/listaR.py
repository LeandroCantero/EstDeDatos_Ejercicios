#Lista Recursiva


class NodoLista:
    def __init__(self,dato = None):
        self.dato = dato
        self.siguiente = None
        
    def imprimir(self):
        print(self.dato, end=" ")
        if self.siguiente != None:
            self.siguiente.imprimir()
            
    def tamanio(self):
        contador = 1
        if self.siguiente != None:
            contador = 1 + self.siguiente.tamanio()
        return contador
        

class Lista:
    def __init__(self):
        self.primero = None
        
    def isEmpty(self):
        return self.primero == None
    
    def append(self, dato):
        nuevo = NodoLista(dato)
        if self.isEmpty():
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo
            
    def vaciar(self):
        self.primero = None
    
    def imprimir(self):
        if not self.isEmpty():
            print(self.primero.dato, end=" ")
            if self.primero.siguiente != None:
                aux = Lista()
                aux.primero = self.primero.siguiente
                aux.imprimir()
            
    def imprimir2(self):
        if not self.isEmpty():
            self.primero.imprimir()
            
    def tamanio(self):
        contador = 0
        if not self.isEmpty():
            contador = self.primero.tamanio()
        return contador
            

