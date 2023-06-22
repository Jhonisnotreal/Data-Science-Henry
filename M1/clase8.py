# Miercoles 17/05/2023

# Algoritmos I

import numpy as np
import random 
import time


'''
import numpy as np

def elMayor():
	for i in range(10):
		x = input(f'{i+1} Digita un numero: ')
		np.array(x)


	maximo = np.max(x)
	return f'el valor mas grande es: {maximo}'
'''

# lista = []

# for i in range(5):
# 	x = input(f'{i+1} Digita un numero: ')
# 	lista.append(x)

# def esMayor(lista):
# 	for i in range(int(lista)):
# 		for y in range(int(lista)):
# 			if y > lista[i]:
# 				mayor = y

# 	return mayor

# print(esMayor(lista))


def maximoElemento(lista):
	maximo = lista[0]

	for elemento in lista:
		if elemento > maximo:
			maximo = elemento

	return maximo 

arreglo = np.random.randint(0,100,50)
lista = []
# for i in range(10):
# 	lista.append(input(f"{i+1} Digita un numero: "))


print(arreglo)
# print(maximoElemento(lista))

# %timeit maximoElemento(arreglo)
print(maximoElemento(arreglo))

def factorial(n):
	factorial = 1 
	for i in range(1, n+1):
		factorial *= i
	return factorial

for i in range(1, 11):
	print(i, "-->", factorial(i))



def primo(numero):
	if numero < 2:
		return False
	for i in range(2, int(numero ** 0.5) + 1):
		if numero % i == 0:
			return False
	return True

print(primo(5))


def extremos(arr):
	maximo = arr[0]
	minimo = arr[0]

	for elemento in arr:
		if elemento > maximo: 
			maximo = elemento

	for elemento in arr:
		if elemento < minimo:
			minimo = elemento

	return f'El maximo es: {maximo} y el minimo es: {minimo}'


print(extremos(arreglo))


def repetidos(arr):
	for elemento1 in arr:
		for elemento2 in arr:
			if elemento1 == elemento2:
				print(elemento1)
				return True

print(repetidos(arreglo))

# Algoritmos de ordenamiento

# Por Insercion

def insertion(arr):
	for i in range(1, len(arr)):

		current = arr[i]
		j = i - 1

		while j >= 0 and arr[j] > current:
			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = current
	return arr

print(insertion(arreglo))

# Por Burbuja

def bubble(arr):
	n = len(arr)

	for i in range(n - 1):
		for j in range(n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	return arr

# lista_azar = random.sample(range(100), 100)

arreglo2 = np.random.randint(200, 300, 50)
print(bubble(arreglo2))











