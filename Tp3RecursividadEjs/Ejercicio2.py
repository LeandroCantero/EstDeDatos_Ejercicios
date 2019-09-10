#Ejercicio 2

'''Una canilla de una casa pierde agua de forma que todos los dias pierde dos
gotas mas que el dia anterior. Escribir una función recursiva que calcule
cuantas gotas perdera la canilla luego de N días, sabiendo que el primer dia
solo perdia 2 gotas.'''

def cuantasGotasPierde(dias):
    gotas = 0
    if dias == 1:
        gotas = 2
    else:
        gotas = 2 + cuantasGotasPierde(dias-1)
    return gotas    
    
    
