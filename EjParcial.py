#Ejercicios parcial

'''
m*n n veces con suma:
'''

def sumarSucesivamente(m,n):
    resultado = 0
    if m>= 0 and n >=0:
        if n == 0:
            resultado = 0
        else:
            resultado = m + sumarSucesivamente(m,n-1)
    else:
        raise Exception("Error")
    return resultado
    



