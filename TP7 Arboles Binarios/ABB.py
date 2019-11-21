#!/usr/bin/python3

"from graphviz import Digraph"

class NodoArbol:
    def __init__(self, dato = None):
        self.data = dato
        self.left = None
        self.right = None

    '''def treePlot(self, dot):
        if self.hasLeft():
            dot.node(str(self.left.data), str(self.left.data))
            dot.edge(str(self.data), str(self.left.data))
            self.left.treePlot(dot)
        if self.hasRight():
            dot.node(str(self.right.data), str(self.right.data))
            dot.edge(str(self.data), str(self.right.data))
            self.right.treePlot(dot)'''

    def setLeft(self, left):
        self.left = left
        
    def setRight(self, right):
        self.right = right
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getData(self):
        return self.data
    
    def insert(self, new):
        if new.getData() < self.getData():
            if self.left == None:
                self.setLeft(new)
            else:
                self.left.insert(new)
        if new.getData() > self.getData():
            if self.right == None:
                self.setRight(new)
            else:
                self.right.insert(new)
    
    def minimo(self):
        if self.left == None:
            minimo = self.data
        else:
            minimo = self.left.minimo()
        return minimo
    
    def maximo(self):
        if self.right == None:
            maximo = self.data
        else:
            maximo = self.right.maximo()
        return maximo
    
    def inOrder(self, node):
        if node == None:
            return
        self.inOrder(node.left)
        print(node.data,end=" ")
        self.inOrder(node.right)
        
    def postOrder(self, node):
        if node == None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data, end=" ")
        
    def preOrder(self, node):
        if node == None:
            return
        print(node.data, end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)
        
    def search(self, new):
        loTiene = "No está en el árbol"
        if self.data == new.data:
            loTiene = "Está en el árbol"
        elif self.data > new.data and self.left != None:
            loTiene = self.left.search(new)
        elif self.data < new.data and self.right != None:
           loTiene = self.right.search(new)
        return loTiene
            
            
            
    
    
class ABB:
    def __init__(self):
        self.root = None

    '''def treePlot(self, fileName='tree'):
        if not self.isEmpty():
            treeDot = Digraph()
            treeDot.node(str(self.root.data), str(self.root.data))
            self.root.treePlot(treeDot)
            treeDot.render(fileName, view=True)''' 
            
    def toEmpty(self):
        self.root = None
        
    def isEmpty(self):
        return self.root == None
    
    def insert(self, dato):
        new = NodoArbol(dato)
        if self.isEmpty():
            self.root = new
        else:
            self.root.insert(new)
                
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
    
    def inOrder(self):
        if not self.isEmpty():
            self.root.inOrder(self.root)
            
    def postOrder(self):
        if not self.isEmpty():
            self.root.postOrder(self.root)
        
    def preOrder(self):
        if not self.isEmpty():
            self.root.preOrder(self.root)
            
    def search(self, dato):
        new = NodoArbol(dato)
        loTiene = "No está en el árbol"
        if self.root.getData() == new.getData():
            loTiene = "Está en el árbol" 
        else:
            loTiene = self.root.search(new)
        return loTiene
        
                
                    
            
            
