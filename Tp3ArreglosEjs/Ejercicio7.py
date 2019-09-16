#Ejercicio 7

'''
Desarrollar una función que elimine la primera aparición de un elemento determinado
de un arreglo de enteros.
'''

def eliminarElemento(array, elemento):
    for i in range(len(array)):
        if array[i] == elemento:
            array[i] = 0
            break
    return array

#Mejor solución:
def eliminarElemento2(array, elemento):
    i = 0
    while array[i] != elemento:
        i += 1
    array[i+1] = 0
    return array
        