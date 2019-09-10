#Ejercicio 1

def factorial(n):
    f = 0
    if n == 0:
        f = 1
    else:
        f = n * factorial(n-1)
        
    return f
