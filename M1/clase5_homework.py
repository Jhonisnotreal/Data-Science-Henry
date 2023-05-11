# 1

'''
1) Implementar un juego, que 
consista en apilar números 
enteros del 1 al 20, de forma 
aleatoria, para lo cual debe 
usarse una estructura de Pila. 
Luego, el usuario debe elegir un 
número de veces en que se va a 
quitar elementos de la pila, los 
cuales, sumados entre sí, no deben 
superar el valor de 50. El usuario 
pierde si la suma supera ese valor. 
Si no lo supera, gana, pero su 
calificación será 10 menos el 
número elementos que falten quitar para 
todavía no superar 50. El programa 
debe informar si perdió, y si ganó, 
con qué calificación lo hizo.
'''

import random

class Pila():

	def __init__(self):
		self.items = []

	def crearPila(self):
		for i in range(20):
			return self.items.append(random.randint(1,20))
		
	def sumar(self, elementos):
		i = 1
		self.suma = 0

		while i <= elementos:
			self.suma += self.items.pop()
			i += 1
		return self.suma

	def puntaje(self, resultado):
		self.puntos = 10
		self.sum_resultado = resultado

		while self.sum_resultado <= 50 :
			self.sum_resultado += self.items.pop()
			self.puntos -= 1

		if self.sum_resultado > 50: 
			return self.puntos += 1
		else: 
			return self.puntos

	def jugar(self):
		print('Cantidad de elementos que deseas quitar de la pila: ')
		self.cantidad_elementos = int(input('Ingresa un numero: '))

		# Creando la pila
		self.crearPila()

		print('Se sacaran', self.cantidad_elementos, 'elementos de la pila')

		self.resultado = self.suma_elementos(self.cantidad_elementos)

		print('La suma es: ', self.resultado)

		if self.resultado > 50:
			print('Perdiste, tus numeros sumaron: ', self.resultado)
		else: 
			print('Ganaste!!, tus numeros son: ', self.resultado)
# 2

'''
2) Implementar un juego donde 
constas de 2 jarras, de capacidad 
5 y 3 litros respectivamente, y 
debes colocar 4 litros en la jarra 
de 5L. Las opciones posibles son:

Llenar la jarra de 3 litros
Llenar la jarra de 5 litros
Vaciar la jarra de 3 litros
Vaciar la jarra de 5 litros
Verter el contenido de la jarra de 
3 litros en la de 5 litros
Verter el contenido de la jarra de 
5 litros en la de 3 litros
'''

class Jarra():
	
	def __init__(self):
		self.jarra3 = 0
		self.jarra5 = 0

	def llenar(self, jarra):
		if jarra == 3:
			if self.jarra3 != 0:
				print('La jarra 3 esta llena')	
			else:
				self.jarra3 = 3
				print('Jarra 3 lts  llenada')

		elif jarra == 5:
			if self.jarra5 != 0:
				print('La jarra 5 esta llena')
			else:
				self.jarra5 = 5
				print('Jarra de 5 lts llenada')

	def vaciar(self, jarra):
		if jarra == 3:
			if self.jarra3 == 0:				
				print('Jarra 3 lts esta vacia') 
			else:
				self.jarra3 = 0
				print('Jarra 3 lts vaciada')

		elif jarra == 5:
			if self.jarra5 == 0:
				print('Jarra 5 lts esta vacia')
			else: 
				self.jarra5 = 0
				print('Jarra 5 lts vaciada')

	def verter(self, jarra):
		if jarra == 3: 
			if self.jarra5 == 0:
				self.jarra5 += self.jarra3
				self.jarra3 = 0

			else:
				while self.jarra3 != 0 and self.jarra5 < 5:
					self.jarra5 += 1
					self.jarra3 -= 1

		if jarra == 5:
			if self.jarra5 == 0:
				pass

			else:
				while self.jarra5 != 0 and self.jarra3 < 3:
					self.jarra3 += 1
					self.jarra5 -= 1

	def consulta(self):
		print('La jarra de 3 lts tiene:', self.jarra3, 'lts. Y la jarra de 5 lts tiene:', self.jarra5, 'lts')


jarras = Jarra()
jarras.llenar(3)

jarras.consulta()
jarras.verter(3)
jarras.consulta()

jarras.llenar(3)
jarras.verter(3)
jarras.consulta()

jarras.vaciar(5)
jarras.consulta()

jarras.verter(3)
jarras.llenar(3)
jarras.verter(3)
jarras.consulta()


