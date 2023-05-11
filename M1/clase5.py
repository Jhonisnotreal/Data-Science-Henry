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

pila = Pila()
pila.push(1)
print(pila.items)
pila.pop()
print(pila.items)


for i in range(10,100, 7):
	pila.push(i)

print(pila.items)
print(pila.peek())

print(pila.items[::-1])

print(' ')
for i  in pila.items[:3:2]:
	print(i)

print(' ')
for i  in pila.items[::-1]:
	print(i)

print(' ')
print(pila.size())
print(' ')

'''
while pila.items:
	print(pila.items)
	print(pila.pop())
	print(pila.empty())
	print(pila.peek())
	print(pila.size())
	print(' ')
	time.sleep(5)
'''

# La Cola agrega (enqueue) al principio (insert) y la
# fila agreaga al finale (append)
class Cola:

	def __init__(self):
		self.items = []
		return None

	def vacio(self):
		return self.items == []

	def enqueue(self, item): #Agregar el elemento eso significa enqueue
		self.items.insert(0, item)
		return None

	def eliminar(self):
		if self.items:
			return self.items.pop()
		else:
			return None

	def tamanio(self):
		return len(self.items)

cola = Cola()
cola.enqueue(1)
print(cola.items)


for i in range(10, 100, 7):
	cola.enqueue(i)
	print(cola.items)
	time.sleep(3)

while cola.items:
	print(cola.items)
	print(cola.eliminar())
	print(cola.vacio())
	print(cola.tamanio())
	time.sleep(3)
