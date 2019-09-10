#Ejercicio1

'''Escribir un programa que le pida al usuario que ingrese N números naturales (primero
uno, luego otro, y así hasta que el usuario ingrese N numeros). Al final, el programa
debe imprimir los números que fueron ingresados en orden inverso, la suma total de
los valores y el promedio.'''

import numpy as np

def imprimirAlReves():
    array = np.zeros(shape=(4),dtype=int)
    array2 = np.zeros(shape=(4), dtype=int)
    sumaTotal = 0
    contador = 0
    print("Ingrese 4 números:")    
    for i in range(len(array)):
        numero = int(input("Numero: "))
        array[i] = numero
    for index in range(len(array)-1,-1,-1):
        sumaTotal += array[index]
        array2[index] = array[contador]
        contador += 1
    promedio = sumaTotal/array.size
    print(array2)
    print("Total:", sumaTotal, "Promedio:", promedio)
    
        
        
        
        
    
        
        
        
