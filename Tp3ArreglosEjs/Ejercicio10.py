#Ejercicio 10

'''
Crear una matriz de tamaño 5x5 y rellenarla de la siguiente forma: la posición M[n,m]
debe contener n+m. Después se debe mostrar su contenido.
'''

import numpy as np

def rellenarMatriz():
    matriz = np.zeros(shape=(5,5),dtype=int)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i,j] = i+j
    return matriz
    
