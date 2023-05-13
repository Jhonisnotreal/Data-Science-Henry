#Lunes 08-05-2023

# Minuto 43 40

import pandas as pd
import numpy as np

lista = ['Matematica', 'Historia', 'Economia','Programacion','Ingles']
series = pd.Series(lista, dtype='string')

print(series[2])

array = np.arange(10,100,10)
serie = pd.Series(array, dtype='float')
# print(serie)

diccionario = {
	'Matematica': 6,
	'Economia': 4,
	'Programacion': 10,
}

series2 = pd.Series(diccionario)
print(series2)

serie3 = pd.Series(np.random.randint(1,10,20))
print(serie3.size)
print(serie3.index)
print(series2.index)
print(serie3[10:15:2])


print(serie3.count())
print(serie3.sum())
print(serie3.cumsum()) #suma acumulativa
print(serie3.value_counts()) #cuantas veces aparece cada valor


print(serie3.max())
print(serie3.min())
print(serie3.mean())
print(serie3.std())
print(serie3.describe()) #Resume todo lo anterior
print(serie3.unique())
print(serie3.value_counts() == 1)
print(serie3.nunique())

serie4 = pd.Series(np.arange(1,5))

print(serie4 + 1) #* ** / etc

def to_string(s):
	return 'valor: ' + str(s)

print(serie4.apply(to_string))
print(serie4[serie4 > 3])

print(serie4[serie4 % 2 == 0])

print(serie3.sort_values())
print(serie3.sort_values(ascending=False).reset_index(drop=True))

print(serie3.sort_index(ascending=False))

serie5 = pd.Series(['A', 'B', None, 'C', np.NaN, 'D'])
print(serie5)

print(serie5.dropna())



datos = {
	'nombre': ['Maria', 'Juan', 'Alizee', 'Luis', 'Logan'],
	'edad': [32,18,19,32,28],
	'grado': ['Economia', 'Medicina', 'Arquitectura', 'Economia', 'Matematicas'],
	'correo': ['maria@gmail.com','juan@gmail.com', 'alizee@gmail.com','luis@gmail.com','logan@gmail.com']
}

df = pd.DataFrame(datos)
print(df)












