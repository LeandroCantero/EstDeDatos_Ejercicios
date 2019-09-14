#Ejercicio 5

'''Desarrollar una función que inserte un elemento en un arreglo de enteros, 
ordenadoen forma ascendente, de forma de no alterar el orden'''

def insertarOrdenado(array, numero):
    i = 0
    while numero > array[i]:
        if(i+1 < len(array)):
            i+=1
        else:
            array[i] = numero
    pos = i
    aux = array[pos]
    for i in range(pos, len(array)-1):
        aux2 = array[i+1]
        array[i+1] = aux
        aux = aux2
    array[pos] = numero
    return array
        
    
