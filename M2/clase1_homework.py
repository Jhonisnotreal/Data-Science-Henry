import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import statistics
import seaborn as sns

# ------Homework
muestra = np.array([[1.85, 1.8, 1.8, 1.8],
					[1.73, 1.7, 1.75, 1.76],
					[1.65, 1.69, 1.67, 1.6],
					[1.54, 1.57, 1.58, 1.59],
					[1.4, 1.42, 1.45, 1.48]])

media = np.mean(muestra)
print("\nMedia: ", media)

'''
Otras formas de calcular la media:
1) 
N = muestra.size()
len(muestra.flatten)
suma = np.sum(muestra)
print(suma / N)

2)
def media(datos):
	return np.sum(datos) / datos.size

print(media(muestra))
'''

mediana = np.median(muestra)
print("\nMediana: ", mediana)

moda = statistics.mode(muestra.flatten())
print("\nModa: ", moda)

'''
def moda(datos):
	lista = list(datos.flatten()) #datos a lista
	conteo = {lista.count(i) for i in lista} #lista de frecuencias de los numeros
	freq_moda = max(conteo)
	return {i for i in lista if lista.count(i) == freq_moda}
	#{} -> son conjuntos

print(moda(muestra))
'''
varianza = np.var(muestra)
print("\nVarianza: ", varianza)

devEstandar = np.std(muestra)
print("\nDeviacion Estandar: ", devEstandar)

# np.sqrt(np.var(muestra)) #otra forma de calcular la devEstandar

lista_muestra = muestra.flatten()
print("\nLista Muestra: ", lista_muestra)

plt.hist(x = lista_muestra, bins = 5, rwidth=0.95, color='#000000')
plt.title('Alturas')
plt.xlabel('Altura (m)')
plt.ylabel('Frecuencia')
plt.show()

# Construye un df y arr para describir la muestra
dic_df = {
	'Ingreso en miles': [10.5, 6.8, 20.7, 18.2, 8.6, 25.8, 22.2, 5.9, 7.6, 11.8],
	'Años de estudio': [17, 18, 21, 16, 16, 21, 16, 14, 18, 18]
	}

df = pd.DataFrame(dic_df)
print(df.describe())
print("\n",df.shape)

# Histograma de 6 secciones para las dos columnas
plt.hist(df['Ingreso en miles'], bins = 6, rwidth = 0.95)
plt.show()

plt.hist(df['Años de estudio'], bins = 6, rwidth = 0.95)
plt.show()

plt.scatter(df['Años de estudio'], df['Ingreso en miles'])
plt.xlabel('Años de estudio')
plt.ylabel('Ingreso en miles')
plt.title('Ingresos x años de estudio')
plt.show()

media_pd = df['Ingreso en miles'].mean()
print("\nMedia pd: ", media_pd)

media_np = np.mean(df['Ingreso en miles'])
print('\nMedia np: ', media_np)

# Agregando [50, 35] y [120, 30] al df. Estos valores extremos afectan mucho el promedio
df.loc[10] = [50, 35]

print("\nMedia afectada: ",df['Ingreso en miles'].mean())

df.loc[11] = [120, 30]
print("\nMedia afectada: ",df['Ingreso en miles'].mean())

# df.loc[12:] = [[10,2], [2,3]] #NO jala x,C


