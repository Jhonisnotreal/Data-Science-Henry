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

while pila.items:
	print(pila.items)
	print(pila.pop())
	print(pila.empty())
	print(pila.peek())
	print(pila.size())
	print(' ')
	time.sleep(5)



