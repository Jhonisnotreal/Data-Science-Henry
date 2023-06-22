import numpy as np
import random as r 
import time

def ListaDesordenada(desorden, cantidad): 
    '''
    Esta función devuelve una lista
    desorden = es un porcentaje de desordenamiento
    cantidad = cantidad de elementos de la lista
    '''

    lista = list(range(0, cantidad))

    desorden = int(cantidad * desorden / 100)

    while (desorden > 0):
        i = r.randint(0,cantidad-1)
        j = r.randint(0,cantidad-1)
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux
        desorden-=1

    return lista


print(ListaDesordenada(90, 20))
print(ListaDesordenada(50, 20))
print(ListaDesordenada(50, 5))

def ord_por_seleccion(lista):
    #completar el código
    return lista

lis = ListaDesordenada(100, 20)
print(lis)

print(ord_por_seleccion(lista))

def ord_por_burbujeo(lista):
	return lista 

print(ord_por_burbujeo(lista))


# 2)
start_time_total = time.time()
total_time_total = time.time() - start_time_total
print("Llevo {} segundos en total.".format(total_time_total))

N = 50000

lis1 = ListaDesordenada(100, N)
lis2 = lis1.copy()
lis3 = lis1.copy()

id(lis1)
id(lis2)
id(lis3)




