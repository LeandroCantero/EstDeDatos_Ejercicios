#Ejercicio 7

def decimalABase2(n):
    numeroN = n
    base2 = 0
    if n == 1 & numeroN % 2 == 1:
        base2 = 1
        print (base2)
    elif n == 1 & numeroN % 2 == 0:
        base2 = 0
        print(base2)
    else:
        base2 = decimalABase2(n//2) % 2
        print (base2)
    return base2