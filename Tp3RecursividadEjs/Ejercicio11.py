#Ejercicio 11

'''
Escribir un programa que pida por teclado una lista de N numeros y los imprima en
forma inversa, es decir, que muestre por pantalla, al finalizar en ingreso de los N
numeros, desde el ultimo hasta el primero. Implementarlo con una funcion recursiva.
'''

import numpy as np

def invertirLista(pos):
    array = np.array([1,2,3,4,5,6,7])
    if pos >= 0:
        print(array[pos])
        invertirLista(pos-1)