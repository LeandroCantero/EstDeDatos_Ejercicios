#Ejercicio 3

'''Si se colocase sobre un tablero de ajedrez, un grano de trigo en el primer casillero,
dos en el segundo, cuarto en el tercero y asi sucesivamente, doblando la cantidad de
granos en cada casilla ¿Cuantos granos de trigo habria en el tablero al final?
Resolver el problema con una función recursiva.
Nota: Pueden pensar la solucion en dos funciones, primero una que calcule la
cantidad de granos de trigo en un casillero determinado y luego otra con el total.'''

def granosPorCasillero(casillero):
    granos = 0
    if casillero == 1:
        granos = 1
    else:
        granos = 2 * granosPorCasillero(casillero -1)
    return granos

def totalTablero(n):
    granosTotales = 0
    if n == 0:
        granosTotales = granosTotales
    else:
        granosTotales = granosPorCasillero(n) + granosPorCasillero(n)
    return granosTotales