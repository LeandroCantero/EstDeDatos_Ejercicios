#Tp Extra 2

'''
1) En un edificio alto, las cucarachas se van distribuyendo por pisos de esta forma: en
el primer piso hay una cucaracha, en los pisos pares el doble del número de piso (p.ej.
en el piso 8 hay 16 cucarachas), en el resto hay la suma de las cucarachas de los dos
pisos anteriores.
Desarrollar un algoritmo que permita determinar la cantidad total de cucarachas en un
edificio que tiene N pisos.
Utilizar Recursividad.
'''

#Primer piso: 1 Cucaracha
#Pisos pares: Doble del piso.
#Resto de los pisos: suma de cucarachas de los 2 pisos anteriores.
#Piso 1 = 1 Total = 1
#Piso 2 = 4 Total = 5
#Piso 3 = 5 Total = 10

def cucarachasEdificio(pisos):
    cucarachas = 0
    if pisos == 1:
        cucarachas = 1
    elif pisos % 2 == 0:
        cucarachas = pisos*2
    else:
        cucarachas = cucarachasEdificio(pisos-2)+cucarachasEdificio(pisos-1)
    return cucarachas
    
def totalCucarachas(pisos):
    cucarachasTotales = 0
    for i in range(pisos):
        cucarachasTotales += cucarachasEdificio(i+1)
    return cucarachasTotales