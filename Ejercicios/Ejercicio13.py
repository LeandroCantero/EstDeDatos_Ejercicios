#Ejercicio13
def main():
    numero = int(input("Ingrese un numero:"))
    primerosPares(numero)
    
def primerosPares(numero):
    resultado = 0
    for i in range(0, numero+1, 2):
        resultado += i
    print(resultado)
    

