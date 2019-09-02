#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:21:07 2019


"""

""" Crear el TAD Propiedad 

-tipo (por defecto un ‘terreno’)
-calle
-altura
-año de construcción (por defecto 0, hasta que se construya)
-ancho del terrno
-largo del terreno
-superficie de construcción (este dato se completa al construir 
   una ‘casa’)



--------

Operaciones:
    
    * Las interfaces para obtener cada dato:  Get....
    * construir en un terreno. En ese momento se registra el año de la construcción,
        la superficie construida y el tipo de construcción (‘casa’ u ‘otro’).
    * Se desea saber para cada propiedad el sentido de circulación de la calle
        - O --> E
        - E --> O
    * Obtener el valor de la propiedad sabiendo que el mt2 tiene un valor de:
             $ 5.000 si es terreno
             $ 10.000 si es casa
             $ 8.000 si es “otro”
    * Indicar si al estar parado en una calle determinada, la propiedad:
            - Está hacia el NORTE, hacia el SUR
            - o en la misma calle
"""

class Propiedad():
    def __init__(self, t = "terreno", c = 0, a = 0, añoDC = 0, anchoDT = 0, 
                 largoDT = 0, supDC = 0):
        self.tipo = t
        self.calle = c
        self.altura = a
        self.añoDeConstruccion = añoDC
        self.anchoDelTerreno = anchoDT 
        self.largoDelTerreno = largoDT
        self.supDeConstruccion = supDC
        
    def getTipo(self):
        return self.tipo
    def getCalle(self):
        return self.calle
    def getAltura(self):
        return self.altura
    def getAñoDeConstruccion(self):
        return self.añoDeConstruccion
    def getAnchoDelTerreno(self):
        return self.anchoDelTerreno
    def getLargoDelTerreno(self):
        return self.largoDelTerreno
    def getSupDeConstruccion(self):
        return self.supDeConstruccion
    
    def construirPropiedad(self, tipo, añoDC, supDC):
        self.tipo = tipo
        self.añoDeConstruccion = añoDC
        self.supDeConstruccion = supDC
    def sentidoCirculacionCalle(self):
        esteAOeste = "Este a Oeste"
        oesteAEste = "Oeste a Este"
        circulacion = ""
        if self.calle%2 == 0:
            circulacion = oesteAEste
        else:
            circulacion = esteAOeste
        return circulacion
    
    def valorPropiedad(self):
        mt2 = self.anchoDelTerreno * self.largoDelTerreno
        valor = 0
        if self.tipo == "terreno":
            valor = mt2*5000
        elif self.tipo == "casa":
            valor = self.supDeConstruccion*10000            
        else:
            valor = mt2*8000
        return valor
    
    def laPropiedadEstaHacia(self, propiedad):
        estaEn = "0"
        if self.calle < propiedad.calle:
            estaEn = "está hacia el Norte"
        elif self.calle > propiedad.calle:
            estaEn = "está hacia el Sur"
        else:
            estaEn = "está en la misma calle"
        return estaEn
        
            
        
    
    

