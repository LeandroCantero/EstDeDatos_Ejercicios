#Expedientes

class Expediente:
    def __init__(self, numExp, tipoCausa, prioridad):
        self.numeroExpediente = numExp
        if self.esCausa(tipoCausa):
            self.tipoCausa = tipoCausa
        else:
            raise Exception("No es una causa válida")
        if self.esPrioridad(prioridad):
            self.prioridad = prioridad
        else:
            raise Exception("No es una prioridad válida")
        
    def esCausa(tipoCausa):
        return tipoCausa == "Civil" or tipoCausa == "Penal" or tipoCausa == "Criminal"
    
    def esPrioridad(prioridad):
        return prioridad == "Normal" or prioridad == "Urgente"
    
    def getCausa(self):
        return self.tipoCausa
    
    def getPrioridad(self):
        return self.prioridad    

    def getNumExp(self):
        return self.numeroExpediente        
        
