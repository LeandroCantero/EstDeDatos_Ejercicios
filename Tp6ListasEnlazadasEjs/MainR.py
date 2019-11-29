#Main LISTAR

import listaR

lista1 = listaR.Lista()

def main():
    print("Está vacía:",lista1.isEmpty())
    lista1.append(5)
    print("Está vacía:",lista1.isEmpty())
    lista1.append(12)
    lista1.append(8)
    lista1.append(9)
    lista1.append(12)
    lista1.append(15)
    lista1.append(18)
    lista1.append(19)
    print(lista1.tamanio())
    lista1.imprimir()

