# Viernes 12 Mayo 2023

# Estructura de datos II
# Listas enlazadas, Tablas Hash

# ---------  Listas enlazadas  ---------

class Nodo:

	def __init__(self, valor):
		self.valor = valor
		self.siguiente = None
		return None

	def getData(self):
		return self.data

	def getNext(self):
		return self.siguiente

	def setData(self, valor):
		self.valor = valor
		return None

	def setNext(self, valor):
		self.siguiente = valor
		return None


class LinkedList:

	def __init__(self):
		self.head = None
		return None

	def estaVacia(self):
		if self.head == None:
			return True
		else:
			return False

	def agregarNodo(self, item):
		nuevo_nodo = Nodo(item)
		nuevo_nodo.setNext(self.head)
		self.head = nuevo_nodo
		return None

	def size(self):
		count = 0
		current = self.head
		while not(current == None):
			count += 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		while (current != None) and (not found):
			if current.getData() is item:
				found = True
			else:
				current.getNext()
		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False

		while (current != None) and (not found):
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if found:
			if previous == None:
				self.head = current.getNext()
			else:
				previous.setNext(current.getNext())				
		else:
			raise ValueError
			print('Valor no encontrado')

	def insert(self, posicion, item):
		if posicion > self.size() - 1:
			raise IndexError
			print('Index out of range')
		current = self.head
		previous = None
		pos = 0
		if posicion == 0:
			self.agregarNodo(item)
		else:
			nuevo_nodo = Nodo(item)
			while pos < posicion:
				pos += 1
				previous = current
				current = current.getNext()
			previous.setNext(nuevo_nodo)
			nuevo_nodo.setNext(current)

	def printLista(self):
		current = self.head
		while not(current == None):
			print(current.getData())
			current = current.getNext()

lista = LinkedList()

print(lista.estaVacia())
print(lista.head)

lista.agregarNodo(1)
nodo1 = lista.head
print(lista.head)
print(nodo1.valor)

print(nodo1.getData())
print(nodo1.getNext())

lista.agregarNodo(2)
# print(lista.head.valor)
# print(lista.head.siguiente)
print(lista.printLista())

print(lista.insert(0,10))