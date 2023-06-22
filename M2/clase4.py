import numpy as np
import pandas as pd
from math import factorial, e
from scipy import stats

# 29/05/2023 = DISTRIBUCION DE PROBABILIDAD

'''
EspacioMuestralMonedas = {(H,H), (H,T), (T,H), (T,T)}

veces que sale cara (H)
(H, H) = 2
(H, T) = 1
(T, H) = 1
(T, T) = 1

esto es variable aleatoria. Para un mismo espacio muestral se puede definir
muchas variables aleatorias. 

veces que sale cara la primera vez:
(H, H) = 1
(H, T) = 1
(T, H) = 0
(T, T) = 0

variable aleatoria - representa una respuesta posible

		DISTRIBUCION DE PROBABILIDAD

N = (H,H) = 2, (H,T) = 1, (T,H) = 1, (T,T) = 0 
P(N = 2) = 1/4
P(N = 1) = 1/2
P(N = 0) = 1/4

esto es distribucion de probabilidades

variable discreta - adquiere valores enteros
variable continua - infinito numero de valores siempre entre 2 valores hay un 3 como la altura

		DISTRIBUCION DE BERNOULLI

Solo 2 resultados posibles

		DISTRIBUCION BINOMIAL

Te apoyas del coeficiente binominal para hallar la cantidad de posibles resultados

'''

def coef_binomial(n, k):
	return factorial(n) // (factorial(k) * factorial(n - k))

def binomial(n, k, p):
	c_bin = coef_binomial(n, k)
	prob = pow(p, k) * pow(1-p, (n-k))

	return c_bin * prob

print(binomial(5, 3, 0.5))

# https://www.geogebra.org/m/jbTtCr7R

'''
		POISSON

Estima el numero de veces que sucede un hecho determinado (ocurrencias) en un intervalo
de tiempo o espacio. Ej:
> NUmero de reparaciones necesarias en 10km de una autopista
> Numero de fugas en 100 km de tuberia

		RELACION DISTRIBUCION BINOMIAL Y POISSON
'''

def poisson(lambda_, k):
	return pow(lambda_, k) * pow(e, -lambda_) / factorial(k)

print(poisson(5, 10))


'''
		DISTRIBUCION HIPERGEOMETRICA

Probabilidades condicionales

'''

def hipergeometrica(N, r, n, x):
	return coef_binomial(r, x) * coef_binomial(N - r, n - x) / coef_binomial(N, n)

print(hipergeometrica(12, 5, 3, 1))


'''
		VARIABLES CONTINUAS

Se dan por una funcion de densidad f(x)

		DISTRIBUCIN NORMAL

Campana de Gauss, aplicaciones: 

peso de personas
altura de personas
puntuaciones de un examen
precipitacion pluvial


'''
mu = 0 #promedio
sigma = 1 
normal = stats.norm(mu, sigma)
print(normal)
print(normal.cdf(2)) #Densidad acumulada, area a la izquierda
print(normal.sf(-1.5)) #Area a la derecha

suma = normal.cdf(-2) + normal.sf(-2) #probabilidad entre los > -2 y menores a -2
print(suma)
