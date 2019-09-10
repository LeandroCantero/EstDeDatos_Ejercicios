#Ejercicio 8

def digitos(n):
    dig = 0
    if n < 10:
        dig = 1
    else:
        dig = 1 + digitos(n//10)
    return dig
