#Ejercicio 5

'''Escribir una funcion recursiva que calcule el numero triangular de indice N (Suma de
los primeros N números enteros). Recordar que:
T (N )=N +T (N −1)'''

def triangular(n):
    tri = 0
    if n == 1:
        tri = 1
    else:
        tri = n + triangular(n-1)
    return tri
    
