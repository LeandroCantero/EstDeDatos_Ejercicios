#Ejercicio 15
'''Escribir un programa que recibe como entrada desde el usuario dos numeros enteros
e informa por pantalla todos los numeros pares entre ellos.'''
def main():
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: "))
    paresEntreN1YN2(n1, n2)
    
def paresEntreN1YN2(n1, n2):
    print("Numeros pares entre",n1,"y",n2,":")
    if(n1 > n2):
        aux = n1
        n1 = n2
        n2 = aux
    for i in range(n1, n2, 2):
        print(i)
        

