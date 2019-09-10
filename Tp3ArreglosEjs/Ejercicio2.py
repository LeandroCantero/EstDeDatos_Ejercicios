#Ejercicio 2

'''Escribir una función recursiva que multiplique todos los elementos de un vector de
enteros.'''

def multiplicarVector(vector, pos = 0):
    multiplicacion = 0
    if pos == len(vector)-1:
        multiplicacion = vector[pos]
    else:
        multiplicacion = vector[pos] * multiplicarVector(vector, pos +1)
    return multiplicacion

