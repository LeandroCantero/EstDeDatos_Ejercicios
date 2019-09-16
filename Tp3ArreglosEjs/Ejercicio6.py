#Ejercicio 6
'''
Desarrollar una función que elimine el elemento que ocupa una determinada posición
de un arreglo de enteros. Al eliminar se debe mantener la continuidad, es decir, los
elementos a la derecha del eliminado, deben desplazarse a la izquierda un lugar.
'''

def eliminarElemento(array, pos):
    array[pos] = 0
    print(array)
    for i in range (pos, len(array)-1):
        print(i)
        array[i] = array[i+1]
    ultimo = len(array)-1
    array[ultimo] = 0
    return array
    

