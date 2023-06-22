# 24/05/2023

# 		PROBABILIDAD
import pandas as pd
import numpy as np
# from math import *
from math import factorial

# Funcion de interes compuesto:
def interes(capitalInicial, i, n):
	valorFinal = capitalInicial*(1+i)**n
	return valorFinal

capital = 120000
i = 0.12
n = 5 
# n es anios

# print(interes(capital, i, n))

# 		ESPACIO MUESTRAL

# Tirar una moneda cara o cruz y un dado de 6 posibilidades
def resultados_posibles(dimen_espacio_muestral:list):
	resultado = 1 #calculando usando productos por eso el 1
	for i in dimen_espacio_muestral:
		resultado *= i
	return resultado

lista = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print(resultados_posibles(lista))

#     		PERMUTACIONES

# Supon que tienes 3 objetos: A, B, C, quiero elegir 2 y de forma ordenada
# Cuantas posibilidades tengo
# 1. Escoge el que quieras. 2. Escoge otro pero no puede ser el que elegiste
# (A, B), (A, C), (B, A), (B, C), (C, A), (C, B)
# Si tengo 5 elementos y elijo c/u, en el 1er paso tengo 5 opciones, en el 2do tengo
# 4, y asi sucesivamente, o sea: 5!

'''
Si tengo 5 elementos y quiero elegir 2 usa esto:
PERMUTACIONES = N! / (N - k)! = 20

5! / (5 - 2)! = 120 / 6 = 20

tengo 20 posibilidades si uso 2 elementos de un conjunto de 5
'''

def permutaciones(N, k):
	return "Tu cantidad de posibilidades son:", factorial(N) // factorial(N - k)

print(permutaciones(52, 2)) #baraja de 52 cartas y saco 2

# 		COMBINACIONES
# Quiero elegir k elementos entre N disponibles pero no importa el orden
# De A, B, C y quiero 2 de 6
# (A, B), (A, C), (C, B)
# 3 posibilidades diferentes

def combinaciones(N, k):
	return "Numero de combinaciones: ", factorial(N) // (factorial(k) * factorial(N - k))

# print(combinaciones(5, 3))
# print(permutaciones(5, 3))
print(combinaciones(2, 2))
print(permutaciones(2, 2))

# Hay una fiesta con 50 personas, en la fiesta por lo menos debe haber 2 personas que cumplen anios el mismo
# dia, una persona apuesta por esto, Debes aceptar la apuesta?

# SOLUCION - Con 1 persona en la fiesta nadie comparte un cumpleanios pues solo hay 1 persona, toma cada anio de 365 dias
# Piensa esto en reversa: Si agrego otra persona entons las posibilidades son 365 / 365 x 364 / 365 y asi hasta prob(noExista) = (365 - n + 1) / 365
# Ahora para el resultado sera 1 - prob(noExistan)

prob = 1.0
asistentes = 50

for i in range(asistentes):
	prob = prob * (365 - i)/ 365

print('La probabilidad de que 2 personas cumplan anios el mismo dia es: ', round((1 - prob) * 100, 2),'%')

