#TDA Cola

import numpy as np

class Cola:
    def __init__(self, capacidad, tipo = int):
        self.cola = np.zeros(shape=(capacidad), dtype = tipo)
        self.fin = None