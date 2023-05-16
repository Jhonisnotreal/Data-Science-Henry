# Estructuras de Datos III

# Arboles

import pandas as pd
import numpy as np

# Los arboles tienen nodos

class Nodo:

	def __init__(self, dato):
		self.valor = dato
		return None

	def setValor(self, dato):
		self.valor = dato

class Arbol:

	def __init__(self):
		self.raiz = None
		self.hijos = []
		return None

	def insertarNodo(self, dato):
		nodo = Nodo(dato)
		if self.raiz == None:
			self.raiz = nodo
			return None
		else:
			nodo_hijo = Arbol()
			nodo_hijo.raiz = nodo 
			self.hijos.append(nodo_hijo)
			return None

	def verRaiz(self):
		return self.raiz 


	def verHijos(self):
		return [self.hijos[i].raiz for i in range(len(self.hijos))]


	def imprimirArbol(self, espacio = 0):
		if self.raiz:
			print('    ' * espacio + str(self.raiz.valor))
			for nodo in self.hijos:
				nodo.imprimirArbol(espacio + 1)
		return None



arbol = Arbol()
arbol.insertarNodo(10)

# print(arbol.raiz)
# print(type(arbol.raiz))

nodo_raiz = arbol.raiz
print(nodo_raiz.valor)
# print(arbol.raiz.valor)

arbol.insertarNodo(20)
arbol.insertarNodo(30)

print(arbol.raiz.valor)

print(arbol.hijos) #Lista de nodos

print([arbol.raiz.valor for arbol in arbol.hijos])

print(arbol.verHijos()[0].valor)

# print(arbol.verRaiz())

print(arbol.imprimirArbol())

arbol.hijos[0].insertarNodo(100)

print(arbol.imprimirArbol())

# arbol.hijos[1].insertarNodo(200)
# arbol.raiz.valor
arbol.raiz.setValor(500)
print(arbol.raiz.valor)
print(arbol.imprimirArbol())

arbol.hijos[0].hijos[0].raiz.valor #el hijo 100
arbol.hijos[0].hijos[0].insertarNodo(1000)

print(arbol.imprimirArbol())

arbol.hijos[1].insertarNodo(300)
print(arbol.imprimirArbol())


# Arbol Binario

class ArbolBinario(Arbol):

	def insertarNodo(self, dato):
		nodo = Nodo(dato)
		if self.raiz == None:
			self.raiz = nodo 

		elif len(self.hijos) < 2:
			nodo_hijo = ArbolBinario()
			nodo_hijo.raiz = nodo 
			self.hijos.append(nodo_hijo)
		else:
			print("NO puede insertarse más nodos en este nivel")
		return None

binario = ArbolBinario()
print(binario.raiz)
binario.insertarNodo(0)
print(binario.raiz.valor)
binario.insertarNodo(10)
binario.insertarNodo(20)
binario.hijos[0].insertarNodo(20)
binario.hijos[1].insertarNodo(50)
binario.hijos[1].insertarNodo(40)
print(binario.imprimirArbol())












