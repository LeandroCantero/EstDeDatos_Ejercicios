#Ejercicio 4

'''
Escribir un programa que permita incorporar en una pila 10 elementos de tipo persona
que contenga nombre, apellido y edad. Pedir por pantalla la cantidad de elementos a
desapilar y mostrar los datos correspondientes.
'''

import pila
import persona

pila3 = pila.Pila(10, persona.Persona)

def incorporarPersona(pila):
    for i in range(pila.length()):
        pila.push(persona.Persona)
    cantDesapilar = int(input("Ingrese cuantos elementos quiere desapilar:"))
    for i in range(cantDesapilar):
        pila.pop()
    print("Tamaño de pila:", pila3.size())

