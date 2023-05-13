#Lunes 08-05-2023

# Minuto 1 28 27

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

df2 = pd.DataFrame([['Maria', 18],['Carmen', 20],['Luis', 22]], columns = ['Nombre', 'Edad'])
print("\n", df2)

# print(df2['Nombre'])

matriz = pd.DataFrame(np.random.randn(4,3), columns=['A', 'B', 'C'])
print("\n", matriz)

# colesterol = pd.read_csv('colesterol.csv', sep=';', decimal=',')
# colesterol.head(7) #las primeras 7, por defecto es 5
# colesterol.tail(7) #las ultimas 5

print("\n", df2.info())
print("\n", df2.shape[1])
print("\n", df2.size)
print("\n", df2.index)
# df.rename(columns={'nombre':'name', 'grado':'estudios'})
# print(df)

# df.rename(index={0:1000, 1:1001, 2:1002})
# print("\n",df)

# print(df.iloc[3:])
print(df.iloc[::2, [0,3]]) #Filas pares con solo las columnas 0 y 3

print("\n", df.loc[:, ['nombre', 'correo']])

print("\n", df[['nombre', 'edad']]) #en [] dobles es el dataframe, con solo 1 es una serie

print("\n", df.nombre)

print("\n", df.loc[3:4, ['nombre', 'edad']])

print("\n", df.loc[df['edad'] > 18])

df['estatura'] = pd.Series([False, False, True, True])

print("\n",df)



