#!/usr/bin/python3

from graphviz import Digraph

class NodoArbol:
    def __init__(self, dato = None):
        self.data = dato
        self.left = None
        self.right = None

    def treePlot(self, dot):
        if self.hasLeft():
            dot.node(str(self.left.data), str(self.left.data))
            dot.edge(str(self.data), str(self.left.data))
            self.left.treePlot(dot)
        if self.hasRight():
            dot.node(str(self.right.data), str(self.right.data))
            dot.edge(str(self.data), str(self.right.data))
            self.right.treePlot(dot)

    def setLeft(self, left):
        self.left = left
        
    def setRight(self, right):
        self.right = right
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def insert(self, dato):
        if self.left == None and dato < self.data:
            self.left = dato
        else:
            self.left.insert(dato)
        if self.right == None and dato > self.data:
            self.right = dato
        else:
            self.right.insert(dato)
    
    def minimo(self):
        if self.left != None:
            minimo = self.left
        else:
            minimo = self.left.minimo()
        return minimo
    
    def maximo(self):
        if self.right != None:
            maximo = self.right
        else:
            maximo = self.right.maximo()
        return maximo
        
    
    
class ABB:
    def __init__(self):
        self.root = None

    def treePlot(self, fileName='tree'):
        if not self.isEmpty():
            treeDot = Digraph()
            treeDot.node(str(self.root.data), str(self.root.data))
            self.root.treePlot(treeDot)
            treeDot.render(fileName, view=True)
            
    def isEmpty(self):
        return self.root == None
    
    def insert(self, dato):
        new = NodoArbol(dato)
        if self.isEmpty():
            self.root = new
        else:
            self.root.insert(dato)
           
    def minimo(self):
        minimo = None
        if not self.tieneIzq():
            minimo = self.root
        else:
            minimo = self.root.minimo()
        return minimo
    
    def maximo(self):
        maximo = None
        if not self.tieneDer():
            maximo = self.root
        else:
            maximo = self.root.maximo()
        return maximo
                    
    def tieneIzq(self):
        return self.root.left != None
    
    def tieneDer(self):
        return self.root.right != None
                
                    
            
            
