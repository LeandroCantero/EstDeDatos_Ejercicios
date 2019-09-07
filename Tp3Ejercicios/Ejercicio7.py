#Ejercicio 7

def decimalABase2(n):
    base2 = 0
    if n == :
        base2 = 0
    else:
        base2 = n % 2 + 10 * decimalABase2(n//2)
    return base2

def aBinario(x):
    if x>1:
        aBinario(x//2)
    print (x%2, end='')
