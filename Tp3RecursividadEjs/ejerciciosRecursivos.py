#Ejercicios recursivo

import numpy as np

#Sumar hasta N

def sumaRecursiva(n):
    res = 0
    if n == 1:
        res = 1
    else:
        res = n + sumaRecursiva(n-1)
    return res

#Recorrer array
    
def recorrerArrRecursiva(pos):
    array = np.array([2,5,7,9,10])
    if pos != len(array):
        print(array[pos])
        recorrerArrRecursiva(pos+1)
        
#Recorrer matriz 
    
def recorrerMatriz(i, j):
    matriz = np.array([[1 , 4 , 2],[10 , 8 , 12],[15, 67, 21]])
    print(matriz[i][j])
    if i != len(matriz)-1 or j != len(matriz[i])-1:
        if j == len(matriz[i])-1:
            i+=1
            j=0
        else:
            j+=1
        recorrerMatriz(i,j)
    