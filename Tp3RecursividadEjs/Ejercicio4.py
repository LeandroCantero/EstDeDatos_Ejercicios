#Ejercicio 4

'''Escribir un programa que pida por teclado un numero natural N y devuelva los
primeros N números de la serie de Fibonacci. Implementar la serie de Fibonacci de
forma recursiva.'''

def fibonacci(n):
    f = 0
    if n <= 2:
        f = 1
    else:
        f = fibonacci(n-2) + fibonacci(n-1)
    return f