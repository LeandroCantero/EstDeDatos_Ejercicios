import ABB

arbol = ABB.ABB()

def main():
    print("Está vacío:", arbol.isEmpty())
    arbol.insert(25)
    print("Está vacío:", arbol.isEmpty())
    arbol.insert(28)
    arbol.insert(29)
    arbol.insert(17)
    arbol.insert(18)
    arbol.insert(15)
    arbol.insert(35)
    print("In-Order")
    arbol.inOrder()
    print()
    print("Pre-Order")
    arbol.preOrder()
    print()
    print("Post-Order")
    arbol.postOrder()
    print()
    print(arbol.search(25))
    print(arbol.search(17))
    print(arbol.search(15))
    '''print(arbol.search(13))'''    
    
