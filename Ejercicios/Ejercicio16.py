#Ejercicio 16
"""
Escribir un programa que pida un numero entero y muestre por pantalla la cantidad de
cifras de dicho numero.
"""

def main():
    num = int(input("Ingrese un numero:"))
    cifrasDeNum(num)
    
def cifrasDeNum(num):
    cifras = 0
    while num > 9:
        num = num/10
        cifras += 1
    print(cifras)
