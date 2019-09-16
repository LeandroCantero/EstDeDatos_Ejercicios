#Ejercicio 11

'''
Desarrollar una función para que, dada una matriz cuadrada de reales de orden N,
obtenga la sumatoria de los elementos que están por encima de la diagonal principal
(excluida ésta).
'''

import numpy as np

def sumarMatrizCuadrada():
    matriz = np.array([[0, 1, 1], [1,0,1], [1,1,0]])
    print(matriz)
    for i in range(len(matriz)):
        contador = i
        for j in range(len(matriz)):
            if i != j and j > contador:
                matriz[i,j] = matriz[i,j] + matriz[i,j]
    return matriz