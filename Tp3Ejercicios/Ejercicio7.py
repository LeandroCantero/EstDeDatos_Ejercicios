#Ejercicio 7

def decimalABase2(n):
    base2 = 0
    if n == 1:
        base2 = 1
    else:
        base2 = n % decimalABase2(n//2)
    return base2
