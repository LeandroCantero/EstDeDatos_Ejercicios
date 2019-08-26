#Ejercicio 12
def main():
    n = int(input("Ingrese un número:"))
    triangular(n)
    
def triangular(n):
    triangular = 0
    for i in range(1, n+1):
        triangular += i
        print(i, " - ", triangular)

