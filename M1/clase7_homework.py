'''
1) Diseñar una clase que permita trabajar con un árbol binario y que contenga los métodos:
* insertaVal: para insertar un dato
* buscaVal: que devuelva True o False si existe o no un dato
* verVal: que imprima por pantalla los valores del árbol
'''


class Nodo():

	def __init__(self, dato):
		self.dato = dato
		self.izq = None
		self.der = None

class Arbol():

	def __init__(self):
		self.raiz = None
		return None

	def insertarVal(self, dato):
		n = Nodo(dato)
		if self.raiz == None:
			self.raiz = n 
		else:
			puntero = self.raiz

			while True:

				if dato < puntero.dato:

					if puntero.izq is None:
						puntero.izq =  n 

					else:
						puntero = puntero.izq

				elif dato > puntero.dato:

					if puntero.der == None:
						puntero.der = n 

					else:
						puntero = puntero.der

				else:
					break  #detengo el programa si es igual

	def buscaVal(self, dato):

		nodo_actual = self.raiz

		while nodo_actual is not None:

			if dato < nodo_actual.dato:

				nodo_actual = nodo_actual.izq

			elif dato > nodo_actual.dato:

				nodo_actual = nodo_actual.der 

			else:
				return True

		return False
	

	def verVal(self, nodo, espacio = 0):
		
		if nodo is not None:
			self.verVal(nodo.izq, espacio + 1)
			print('       ' * espacio + str(nodo.dato) + '\n')
			self.verVal(nodo.der, espacio + 1)


a = Arbol()
# a.insertarVal(2)
for i in range(-10, -50, -10):
	a.insertarVal(i)
for i in range(10, 50, 10):
	a.insertarVal(i)
for i in range(-45, 50, 10):
	a.insertarVal(i)

for i in range(-47, 50, 5):
	a.insertarVal(i)

# print(a.raiz.dato)
print(a.verVal(a.raiz))
# print(a.raiz.izq.dato)

print(a.buscaVal(5))				
# print(a.raiz.izq.dato)
# a.raiz.izq.dato = 199
# print(a.raiz.izq.dato)
# print(a.verVal(a.raiz))

print(a.buscaVal(-12))






