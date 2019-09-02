#Ejercicio 18
'''Escribir un programa que imprima por pantalla los numeros desde el 32 al 64, en
todas lasbases desde 2 hasta 16. Se debe imprimir un numero por fila en las 15
bases distintas separados por el carácter tabular (“\t”). Nota: Los numeros se pueden
imprimir en orden inverso.'''

def main():
    numero = 32
    base = 2
    
    while numero>=base:
        resto = numero%base
        numero = numero//base
        print(resto, end = "")
    print(numero)
    
def printNums():
    
    
