#Ejercicio 17
import math
'''Escribir un programa que pida un numero entero e informe si dicho numero es primo
o no primo. Nota: Ningun numero es divisible por un numero mayor a la raiz cuadrada
de si mismo.'''

def main():
    numero = int(input("Escriba un numero:"))
    esPrimo(numero)

def esPrimo(numero):
    primo = "Es primo"
    raizNumero = int(math.sqrt(numero))
    for i in range(raizNumero, numero):
        if(numero%i == 0):
            primo = "No es primo"
    print(primo)
            
            
            
    
            
