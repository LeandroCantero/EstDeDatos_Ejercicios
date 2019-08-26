#Ejercicio10
def main():
    print("Numeros divisibles por 2 y por 3")
    divisiblesPor()
    
def divisiblesPor():
    for i in range(1, 101):
        if(i%2 == 0 and i%3 == 0):
            print(i)
            

