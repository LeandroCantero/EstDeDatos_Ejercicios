#Ejercicio 7

def decimalABase2(n):
    base2 = 0
    if n == 0:
        base2 = 0
    else:
        base2 = n % 2 + 10 * decimalABase2(n//2)
    return base2
