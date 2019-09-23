#Ejercicio 2

'''
Realizar un programa que muestre la cantidad de elementos de una pila de enteros.
Mostrar y desapilar 2 elementos y volver a imprimir el tamaño de la pila.
'''
import pila

pila1 = pila.Pila(5, int)
pila1.push(3)
pila1.push(5)

def cantidadElementos(pilaEnteros):
    print(pilaEnteros.size())
    pilaEnteros.printStack()
    print("")
    for i in range(2):
       pilaEnteros.pop()
    print(pilaEnteros.size())
    
