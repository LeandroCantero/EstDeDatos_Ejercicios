#Ejercicio 9

'''
Crear y cargar dos matrices de tamaño 3x3, sumarlas y mostrar su suma.
'''

import numpy as np

def sumarMatrices(matriz1, matriz2):
    matriz3 = np.zeros(shape=(3,3),dtype=int)    
    for i in range(len(matriz1)):
        for j in range(len(matriz2)):
            if i == j:
                matriz3[i] = matriz1[i] + matriz2[j]
                print(matriz3)
    return matriz3
            

