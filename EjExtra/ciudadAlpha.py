#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:50:20 2019

@author: fernandopuricelli
"""
## OJO: este import supone que el Tipo de Datos está guardado en propiedad.py 
## en el mismo directorio
import propiedad

""" ------------------- IMPORTANTE --- no cambiar nada desde acá"""
import matplotlib.pyplot as plt

def enPlanoDeCatastro(calle,altura):
    plt.plot(altura, calle, color='green', marker='o', linestyle='dashed',linewidth=2, markersize=24)

def ciudadAlphaEnPlano():
    plt.ylim(0,5)
    plt.xlim(0,10)
    plt.grid(True)
    plt.show()
"""  -----------------  hasta acá"""

# COMPLETAR (0): crear la función impuestoRenta que recibe una propiedad
# y retorna el impuesto a pagar . siguiendo la siguiente fórmula
# es el 10% del valor de la propiedad 

# ....
def impuestoRenta(p):
    impuesto = p.valorPropiedad() * 10 /100
    return impuesto

# hasta aquí completar (0)

""" ------------------- IMPORTANTE --- no cambiar nada desde acá"""
plt.figure()
"""  -----------------  hasta acá"""

# COMPLETAR (1): crear 3 propiedades

# ....
propiedad1 = propiedad.Propiedad("terreno", 3, 7, 0, 10, 20, 0)
propiedad2 = propiedad.Propiedad("terreno", 2, 4, 0, 20, 15, 0)
propiedad3 = propiedad.Propiedad("terreno", 5, 1, 0, 10, 30, 0)

# Hasta aquí completar (1)

# COMPLETAR (2): construir en el año 1990 134mts en la propiedad 1
#  y construir en el año 2005 180mts en la propiedad 2

# ....
propiedad1.construirPropiedad("casa", 1990, 134)
propiedad2.construirPropiedad("casa", 2005, 180)


# hasta aquí completar (2)

# COMPLETAR (3): usar la primitiva de catastro (enPlanoDeCatastro) para ubicar en el mapa las
# 3 propiedades

# ....
enPlanoDeCatastro(3,7)
enPlanoDeCatastro(2,4)
enPlanoDeCatastro(5,1)


# hasta aquí completar (3)


""" ------------------- IMPORTANTE --- no cambiar nada desde acá"""
ciudadAlphaEnPlano()
"""  -----------------  hasta acá"""

# COMPLETAR (4): imprimir el tipo, dirección y sentido de circulación de las 3 propiedades

# ....
print("Propiedad 1:")
print("Tipo:", propiedad1.getTipo())
print("Dir:", "Altura:", propiedad1.getAltura(), "Calle:",propiedad1.getCalle())
print("Sentido de circulacion:", propiedad1.sentidoCirculacionCalle())
print("")
print("Propiedad 2:")
print("Tipo:",propiedad2.getTipo())
print("Dir:", "Altura:", propiedad2.getAltura(), "Calle:", propiedad2.getCalle())
print("Sentido de circulacion:", propiedad2.sentidoCirculacionCalle())
print("")
print("Propiedad 3:")
print("Tipo:",propiedad3.getTipo())
print("Dir:", "Altura:", propiedad3.getAltura(), "Calle:", propiedad3.getCalle())
print("Sentido de circulacion:", propiedad3.sentidoCirculacionCalle())
print("")
print("-----------------")
print("")


# hasta aquí completar (4)

# COMPLETAR (5): imprimir la valuación de las 3 propiedades

# ....
print("Propiedad 1:")
print("Valor:", propiedad1.valorPropiedad())
print("")
print("Propiedad 2:")
print("Valor:", propiedad2.valorPropiedad())
print("")
print("Propiedad 3:")
print("Valor:", propiedad3.valorPropiedad())
print("")
print("---------")
print("")


# hasta aquí completar (5)

# COMPLETAR (6): partiendo de la calle 1 mostrar hacia qué dirección se debe ir
# para llegar a cada propiedad

# ....

posicion1 = propiedad.Propiedad("otro", 1, 0, 0, 0, 0, 0)

print("La propiedad 1", posicion1.laPropiedadEstaHacia(propiedad1))
print("La propiedad 2", posicion1.laPropiedadEstaHacia(propiedad2))
print("La propiedad 3", posicion1.laPropiedadEstaHacia(propiedad3))

# hasta aquí completar (6)

# COMPLETAR (7): con la función creada en COMPLETAR (0) imprimir los impuestos
# a cobrar a cada una de las propiedades

# ....
print("")
print("--------")
print("")
print("Imouestos de la propiedad 1:", impuestoRenta(propiedad1))

print("Imouestos de la propiedad 2:", impuestoRenta(propiedad2))

print("Imouestos de la propiedad 3:", impuestoRenta(propiedad3))


# hasta aquí completar (7)





