#Ejercicio 16

'''
Escribir un programa que reciba una pila de enteros y genere dos pilas, una con solo
los numeros pares y otra con solo los impares, provenientes de la pila de entrada.
'''

import pila

pila1 = pila.Pila(5, int)
for i in range(5):
    pila1.push(i)
pila2 = pila.Pila(5, int)
pila3 = pila.Pila(5, int)

def paresImpares(pila):
    while not pila1.isEmpty():
        if pila1.top()%2 == 0:
            pila2.push(pila1.pop())
        else:
            pila3.push(pila1.pop())
        
    
