#Ejercicio 4

'''Desarrollar una función que inserte un elemento en un arreglo de enteros, dada la
posición de inserción, al insertar un elemento en una posición, se produce un
desplazamiento a la derecha, si el arreglo estaba lleno, el ultimo elemento se pierde.'''


def insertarNumeroEn(array, numero, pos):
    aux = array[pos]
    for i in range(pos, len(array)-1):
        aux2 = array[i+1]
        array[i+1] = aux
        aux = aux2
    array[pos] = numero
    return array   
        
            
        
    

