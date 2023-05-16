class Nodo():

	def __init__(self, dato):
		self.dato = dato
		self.izq = None
		self.der = None

class Arbol():

	def __init__(self):
		self.raiz = None

	def insertarVal(self, dato):
		n = Nodo(dato)
		if self.raiz == None:
			