#Lista

class NodoLista:
    def __init__(self,dato = None):
        self.dato = dato
        self.siguiente = None

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
        contador+=1
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
            for i in range(pos):
                aux = aux.siguiente
        return aux.dato
    
    def append(self, dato):
        nuevo = NodoLista(dato)
        if self.isEmpty():
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo
    #    
    def reemplazar(self, dato, pos):
        nuevo = NodoLista(dato)
        aux = self.primero
        if pos == 0:
            aux = aux.siguiente
            self.primero = nuevo
            nuevo.siguiente = aux
        elif pos == 1:
            aux2 = aux.siguiente.siguiente
            aux.siguiente = nuevo
            nuevo.siguiente = aux2
        else:
            for i in range(pos):
                aux = aux.siguiente
            aux2 = aux.siguiente
            aux = nuevo
            nuevo.siguiente = aux2
            
            
                        
    def eliminarElemento(self, pos):
        aux = self.primero
        if pos == 0:
            aux2 = aux.siguiente
            aux = None
            self.primero = aux2
        elif pos == 1:
            aux.siguiente = aux.siguiente.siguiente
        else:
            for i in range(pos-1):
                aux = aux.siguiente
            aux.siguiente = aux.siguiente.siguiente 
            
    def clonar(self, lista):
        for i in range (self.tamanio()):
            lista.append(self.obtenerElemento(i))
        
        
    def imprimir(self):
        aux = self.primero
        if aux.siguiente == None:
            print(aux.dato)
        while aux.siguiente != None:
            print(aux.dato, end=" ")
            aux = aux.siguiente
        print(aux.dato)
        
    #Ejercicio 2
    #def intercambiarPrimeros(self):
    
    #Ejercicio 3
    def expandirLista(self, lista):
        for i in range(lista.tamanio()):
            self.append(lista.obtenerElemento(i))
        
    #Ejercicio 4
    
        
        