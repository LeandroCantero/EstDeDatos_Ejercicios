#Ejercicio 6

'''Escribir una función recursiva que calcule las combinaciones de N elementos tomados
de a M...'''

def combinatorio(n, m):
    c = 0
    if m == 1:
        c = n
    elif n == m:
        c = 1
    elif n > m and m>1:
        c = combinatorio(n-1, m-1) + combinatorio(n-1, m)
    return c
        