#Miercoles 10-05-2023

# Estructuras de Datos 1 - Pilas y Colas

import time 

class Pila:

	def __init__(self):
		self.items = []
		return None

	def empty(self):
		return self.items == [] 

	def push(self, item): #Agregar item a la lista
		self.items.append(item)
		return None

	def pop(self):
		return self.items.pop()

	def peek(self):
		if self.items:
			return self.items[-1]
		else:
			return None

	def size(self):
		return len(self.items)


