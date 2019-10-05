#Ejercicio integrador

import numpy as np
import expediente
import cola

'''
 recibirExpediente(exp) : Agrega en expediente que recibe por parámetros a la cola que corresponde a su
prioridad
 primerExpedienteATratar() : Si hay trámites urgentes, devuelve el expediente a extraer de la cola
correspondiente, caso contrario, el expediente a extraer de los normales.
 tratarPrimerExpediente() : Desencola el expediente de la cola en la que está, y lo devuelve.
 cantidadDeExpedientes() : Cantidad total de expedientes, sumando las dos colas.
- cantidadPor Tipo(tipoExp) : Calcula la cantidad de expedientes de tipo tipoExp en cada una de las colas y
retorna un arreglo con ambos valores.
- estaComplicado() : Indica si tiene más de 50 expedientes por tratar en total.
- cambiaDeEstado(nroExp) : Cambia de estado el expediente de número nroExp (de “Normal” a “Urgente” o
viceversa), en consecuencia, debe cambiarlo de cola.
'''

class Juzgado:
    def __init__(self, colaUrgente, colaNormal):
        urgente = cola.Cola(50, expediente.Expediente)
        normal = cola.Cola(50, expediente.Expediente)
        self.colaUrgente = urgente
        self.colaNormal = normal
        
    def recibirExpediente(self, expediente):
        if expediente.getPrioridad() == "Normal":
            self.colaNormal.queue(expediente)
        else:
            self.colaUrgente.queue(expediente)
    
    def primerExpedienteATratar(self):
        expAExtraer = expediente.Expediente
        if expediente.getPrioridad() == "Urgente":
            expAExtraer = self.colaUrgente.top()
        else:
            expAExtraer = self.colaNormal.top()
        return expAExtraer

    def tratarPrimerExpediente(self):
        if not self.colaUrgente.isEmpty():
            self.colaUrgente.dequeue()
        else:
            self.colaNormal.dequeue()
            
    def cantidadDeExpedientes(self):
        return self.colaNormal.size() + self.colaUrgente.size()
    
    def cantidadPorTipo(self, tipExp):
        array = np.zeros(shape=(self.colaNormal.size()), dtype = int)
        for i in range(len(array)):
            
            
        
        
        
        
