#Main

import lista

lista1 = lista.Lista()
listaMen = lista.Lista()
listaMay = lista.Lista()
listaIgu = lista.Lista()
lista3 = lista.Lista()

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
    lista1.reemplazar(4,6)
    lista1.imprimir()
    invertirLista(lista1)
    "duplicarLista(lista1)"
    mezclarListas(lista1, lista1)
 
    
def tresListas(lista, k):
    for i in range (lista.tamanio()):
        if lista.obtenerElemento(i) > k:
            listaMay.append(lista.obtenerElemento(i))
        elif lista.obtenerElemento(i) < k:
            listaMen.append(lista.obtenerElemento(i))
        else:
            listaIgu.append(lista.obtenerElemento(i))
    listaMay.imprimir()
    listaMen.imprimir()
    listaIgu.imprimir()
    
def invertirLista(lista):
    j = lista.tamanio()-1
    for i in range (lista.tamanio()//2):
        aux = lista.obtenerElemento(j)
        lista.reemplazar(lista.obtenerElemento(i), j)
        lista.reemplazar(aux, i)
        j = j-1
    lista.imprimir()
    
def duplicarLista(lista):
    for i in range(lista.tamanio()):
        lista.append(lista.obtenerElemento(i))
    lista.imprimir()

def mezclarListas(lista, lista2):
    for i in range(lista.tamanio()):
        lista3.append(lista.obtenerElemento(i))
        lista3.append(lista2.obtenerElemento(i))
    print("----------------------------------")
    lista3.imprimir()
    print(lista3.tamanio())

            
            
    
    
    
    