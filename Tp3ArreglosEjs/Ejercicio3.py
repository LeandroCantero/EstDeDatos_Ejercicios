#Ejercicio 3

'''Crear un programa que lea por teclado N números enteros y los desplace una
posición hacia la derecha: el primero pasa a ser el segundo, el segundo pasa a ser el
tercero y así sucesivamente. El último pasa a ser el primero. Guardar los numeros
ingresados en un arreglo en el orden original y luego correrlos dentro del mismo
arreglo. Mostrarlos antes y despues por pantalla.'''

import numpy as np

def moverALaDerecha():
    cantidadNum = int(input("Cuantos numeros desea ingresar:"))
    array = np.zeros(shape=(cantidadNum), dtype = int)
    aux = array[0]
    #Ingreso de datos
    for pos in range(len(array)):
        numero = int(input("Numero:"))
        array[pos] = numero
    #Mover numeros a la derecha
    for i in range(len(array)-1):
        aux2 = array[i+1]
        array[i+1] = aux
        aux = aux2
    array[0] = aux
    print(array)
#
def moverALaDerecha2():
    array = np.array([[1, 4, 6]])
    aux = array[len(array)-1]
    for i in range(len(array)-1, 0, -1):
        array[i] = array[i-1]
    array[0] = aux
    print(array)