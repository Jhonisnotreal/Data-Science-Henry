# Viernes 5/05/2023


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

uniforme = np.random.uniform(low=0, high=1, size=100)
# print('Uniform: ',uniforme)

# plt.hist(uniforme, bins = 10, rwidth = 0.85) #bins - intervalos


enterosAleatorios = np.random.randint(1,10, (3,2))
print('Enteros Aleatorios:', enterosAleatorios)

distNormal = np.random.randn(2,2)
print('Distribucion Nomal', distNormal)

# plt.hist(distNormal, bins = 100)


matriz1 = np.array([[1,2,3],[4,5,6]])
matriz1.flatten()
print('Matriz 1',matriz1)

# print(matriz1 * 10)

matrix = np.array([[2,3],[2,3],[2,3]])
matrix2 = np.array([[1,6,5,2,8],[1,2,7,0,9]])

print(np.matmul(matrix, matrix2))

mat = np.mat([[1,2,3],[4,5,6]])
print(type(mat))
print(mat.T)

x = np.mat(np.arange(4).reshape((2,2)))
z = x-1j* x

print(x)
print('Numeros complejos',z)
print('Matriz conjugada',z.H)

mat1 = np.mat([[1,2],[0,9]])
print('Matriz inversa',np.matmul(mat1, mat1.I))

lista_ = np.random.randint(50,80, size=30)
print('El valor medio', np.mean(lista_))
print('El valor mediana', np.median(lista_))
print('El valor deviacion estandar', np.std(lista_))
print('El valor percentil', np.percentile(lista_, 90))
print('El valor maximo', np.max(lista_))
print('El valor minimo', np.min(lista_))


# -------------------------------------------------------------
# Homework
# Ejercicio 1
lista = [1,2,3,4]
arr = np.array([1,2,3,4])

lista.append(5)
arr2 = np.append(arr, 5)

print(lista)
print(arr2)

print(arr2 ** 2)

print('Arreglo de (n,)')
arreglo = np.array([1,2,3,4,5,6])
print(arreglo,'. Shape =', arreglo.shape, "\n")

print('Arreglo de (2,n)')
arreglo = np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]]) 
print(arreglo,'. Shape =', arreglo.shape, "\n")

print('Arreglo de (n,1)')
arreglo = np.array([[1,2,3,4,5,6]]) 
print(arreglo.T,'. Shape =', arreglo.T.shape, "\n")

# Ejercicio 2
numeros = np.arange(0,10)
arreglo4 = np.linspace(0,100, 100)
# equispaciados = np.linspace(numeros, 10)

# print(numeros)
print(arreglo4)
# print(equispaciados)


# Ejercicio 3

arreglo3 = np.arange(10,101)
mascara = ((arreglo3 % 3) == 0)

print(arreglo3[mascara])

# Ejercicio 4
zeros = np.zeros((5,10))

# print(zeros)

zeros[[1,3],:] = 1
zeros[:,[2,7]] = 2

print(zeros)