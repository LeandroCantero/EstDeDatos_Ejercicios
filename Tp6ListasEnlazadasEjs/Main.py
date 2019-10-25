#Main

import lista

lista = lista.Lista()
listaDos = Lista()
listaVacia = Lista()

def main():
    print("Está vacía:",lista.isEmpty())
    lista.append(5)
    print("Está vacía:",lista.isEmpty())
    lista.append(12)
    lista.append(8)
    lista.append(9)
    lista.append(12)
    lista.imprimir()
    listaDos.append(15)
    listaDos.append(12)
    listaDos.append(12)
    print("Lista 2:")
    listaDos.imprimir()
    lista.expandirLista(listaDos)
    print("Lista expandida:")
    lista.imprimir()
    lista.clonar(listaVacia)
    print("Lista vacía:")
    listaVacia.imprimir()    
    
    
    
    
    