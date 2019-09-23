#Ejercicio 6

'''
Escribir
una funcion que invierta el orden de una pila. No debe devolver una
nueva pila invertida, sino invertir lo valores de la pila que ingresa por parametros.
'''
import pila
import numpy as np

pilaI = pila.Pila(5, int)
for i in range(len(pilaI.pila)):
    pilaI.push(i*2)

def invertirPila(pila):
    vector = np.zeros(shape=(pila.size()), dtype = int)
    print("Pila:")
    pila.printStack()
    for i in range(pila.size()):
        vector[i] = pila.top()
        pila.pop()
    for i in range(len(vector)):
        pila.push(vector[i])
    print("")
    print("Pila invertida:")
    pila.printStack()
    
    

