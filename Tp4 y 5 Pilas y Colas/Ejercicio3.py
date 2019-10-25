#Ejercicio 3

'''
Escriba un programa que permita el ingreso de N numeros enteros y los guarde en
una pila. Luego al terminar, muestre por pantalla (al ser desapilados), los numeros
ingresados.
'''

import pila

def mostrarNumsIngresados():
    indice = int(input("¿Cuantos números desea ingresar?"))
    pila2 = pila.Pila(indice, int)
    #Ingreso de datos
    for i in range(indice):
        numero = int(input("Ingrese un número:"))
        pila2.push(numero)
    #Programa
    for i in range(indice):
        pila2.pop()
    pila2.printStack()
    