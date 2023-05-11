# Viernes 5/05/2023

# Min 46 23

import numpy as np
import matplotlib.pyplot as plt

lista_np = np.array([1,3,4,5]) #Si escribes uno de tipo float todos se vuelven float
print('Lista 1:', lista_np)
print('Tipo de dato',lista_np.dtype)

lista2 = np.arange(16, 36, 2)   #np.arange(25)
print('Lista 2', lista2)
print('Cuarto y quinto elementos:',lista2[3:5])

# Cambiar la forma reshape
print('2 filas y 5 columnas',lista2.reshape(2,5))

tensor = np.arange(1, 13)
print(tensor.reshape(3,2,2))


alreves = [1,3,4,5,6]
alreves2 = np.array(alreves) #de lista a array

#intervalo con subdivisiones/partes - linspace
subdivisiones = np.linspace(10,15,20)
print(subdivisiones)

# plt.plot(subdivisiones, '+')

ceros = np.zeros(8, dtype=float).reshape(4,2)
print(ceros)

unos = np.ones(6).reshape(3,2)

#alternativa, al inicio va el reshape y despues el numero que rellena
full = np.full((3,2), 4)
print(full)

full2 = np.full((3,2), np.pi) #np.nan
print(full2)


aleatorio = np.random.rand(2,2) #rand - no. entre 0 y 1
print(aleatorio)

uniforme = np.random.uniform(low=0, high=1, size=6)
print('Uniform: ',uniforme)






# -------------------------------------------------------------
# Homework
# Ejercicio 1

# Ejercicio 2
numeros = np.arange(0,10)

# print(numeros)

# Ejercicio 3

# Ejercicio 4
zeros = np.zeros((5,10))

# print(zeros)