#Ejercicio 2

'''
Realizar un programa que muestre la cantidad de elementos de una pila de enteros.
Mostrar y desapilar 2 elementos y volver a imprimir el tamaño de la pila.
'''
import numpy as np
import pila

pila1 = pila.Pila(5)
pila1.push(3)
pila1.push(5)

def cantidadElementos(pilaEnteros):
    p = pilaEnteros.pila
    vector = np.zeros(shape=(len(p)), dtype = p.dtype)
    print(len(vector))
    print(p)
    for i in range(2):
       pila1.pop()
       print(p)
    
