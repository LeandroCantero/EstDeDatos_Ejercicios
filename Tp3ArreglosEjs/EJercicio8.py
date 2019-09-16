#Ejercicio 8

'''
Desarrollar una función que elimine todas las apariciones de un determinado
elemento de un arreglo de enteros.
'''

def eliminarElementoTodos(array, elemento):
    for i in range(len(array)):
        if array[i] == elemento:
            array[i] = 0
    return array