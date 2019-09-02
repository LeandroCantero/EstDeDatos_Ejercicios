import math
#Ejercicio14
'''Escribir un programa que recibe como entrada desde el usuario los valores de a , b y c
de un polinomio de grado 2, e informa las raices (reales y complejas).'''
def main():
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    disc = b**2-4*a*c
    cuenta1= (-1)*b/2*a
    if disc >=0:
        r1 = cuenta1 + math.sqrt(disc)/2*a
        r2 = cuenta1 - math.sqrt(disc)/2*a
        print(r1)
        print(r2)
    else:
        preal= cuenta1
        pimg= math.sqrt(abs(disc)/2*a)
        print(preal,"+i", pimg)
        print(preal, "-i", pimg)

    

