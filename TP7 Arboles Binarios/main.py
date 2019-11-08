import ABB

arbol = ABB.ABB()

def main():
    print("Está vacío:", arbol.isEmpty())
    arbol.insert(25)
    print("Está vacío:", arbol.isEmpty())
    arbol.insert(28)
    
