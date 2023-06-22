# 22/05/2023

# Estadistica
# Estadistica Descriptiva

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import statistics
import seaborn as sns
import random

emisiones = pd.read_csv('Emisiones_CO2.csv', sep='|', decimal=',', thousands='.', encoding='Latin-1')
emisiones.dropna(inplace=True)
# print(emisiones.sample(10)) #muestra de 10 datos aleatorios

#----FRECUENCIAS-----

autos_vendidos = {
	"Marca": ["Audi", "BMW", "Mercedes"],
	"Cantidad (Frecuencia Absoluta)": [124, 98, 113]
}

df = pd.DataFrame(autos_vendidos)

total_vendidos = sum(df['Cantidad (Frecuencia Absoluta)'])
# Otra forma de calcular la suma total de la columna 'Cantidad' del df:
# df['Cantidad (Frecuencia Absoluta)'].sum()
# np.sum(df['Cantidad (Frecuencia Absoluta)'])

print('Soy total vendidos:\n', total_vendidos)

# Frecuencia relativa
frecuenciaR_audi = 124/total_vendidos
print('\nSoy frecuencia Relativa de Audi\n',frecuenciaR_audi)

def frequenciaRelativa(datos):
	total = np.sum(datos)
	return datos/total

datos = df['Cantidad (Frecuencia Absoluta)']
df['Frecuencia Relativa'] = frequenciaRelativa(datos)
print('\nSoy df de los autos\n', df)

# plt.bar(df['Marca'], df['Cantidad (Frecuencia Absoluta)'])
# plt.show()

# Ejemplo 2
valores = ['M', 'R', 'B', 'MB', 'E']

calificaciones = [random.choice(valores) for i in range(75)] #simular valores que no tengo
print('\nCalificaciones: \n', calificaciones)
conteo = [calificaciones.count(i) for i in valores]
print('\nConteo de Calificaciones\n',conteo)

conteo_dic = {
	'Calificacion': valores,
	'Frecuencia Absoluta': conteo
}

df2 = pd.DataFrame(conteo_dic)
print('\nDf de calificaciones\n',df2)

df2['frecuencia relativa'] = frequenciaRelativa(df2['Frecuencia Absoluta'])
print('\nDf de calificaciones actualizado\n',df2)

df2['fr. abs. acumulada'] = df2['Frecuencia Absoluta'].cumsum()
df2['fr. rel. acumulada'] = df2['frecuencia relativa'].cumsum()
print('\nDf2 de Calificaciones completo\n',df2)

def frecuencia_acumulada(datos):
	acumulado = 0
	f_acum = []
	for i in datos:
		acumulado += i
		f_acum.append(acumulado)
	return f_acum

# print(frecuencia_acumulada(df2['Frecuencia Absoluta']))
# print(frecuencia_acumulada(df2['frecuencia relativa']))

#Histograma

data = [1.2,2.3,2.4,3.5,5.32,6.0,7.7,8.2,8.2,9.1,9.1]

# plt.hist(x=data, bins=5, rwidth=0.85, color='black')
# bins son cantidad de partes en que divido el intervalo, o sea en gpos de 5 o 6 
# plt.show()

# MEDIDAS DE TENDENCIA CENTRAL

# MEDIA ARITMETICA (PROMEDIO)

def media(datos):
	return np.sum(datos) / len(datos)

print("\nLa media aritmetica de 'Data' es: ",media(data))

np.mean(data) # da lo mismo que la funcion 'media'

emisiones['CO2 (kt)'].mean()

# MEDIANA
data1 = [1,2,2,3,5,6,7,8,8,9,9]
data2 = [1,2,2,3,5,6,7,8,8,9]


def mediana(datos):
	datos_ordenados = sorted(datos)
	posicion = len(datos)//2 #el elemento con el indice que de este numero
	if len(datos) % 2 == 1: #si es impar
		return datos[posicion]
	else:
		return (datos[posicion - 1] + datos[posicion]) / 2 #la posicion por indice le resto 1 para tener el valor anterior y lo suma
		# con el valor ya que obtuve, luego lo divido para tener le mediana

print("\nAqui la mediana: \n",mediana(data1))		
print("\n",mediana(data2))

# MODA
data3 = [1,2,2,3,5,6,7,8,8,8,9,9]
# counting = [data3.count(i) for i in data3] #list operation []
counting = {data3.count(i) for i in data3} #set operation {}, evito las repeticiones
print(counting)

frecuencia_moda = max(counting)
print("El dato mas frecuente aparece:",frecuencia_moda,"veces")

moda = {i for i in data3 if (data3.count(i) == frecuencia_moda)}
print(moda)

# 		DISPERSION
# RANGO (diferencia entre max y min)

print(max(data1))
print(min(data1))

print(max(emisiones['CO2 (kt)']))
print(np.min(emisiones['CO2 (kt)']))


# VARIANZA cada valor lo resta 
# con la media y el resultado lo eleva al 2, y los suma todos
# y todo se divide entre n cantidad que tengo


def varianza(datos):
	media = np.mean(datos)
	diferencias = [(i - media)**2 for i in datos]
	suma = np.sum(diferencias)
	return suma / len(datos)

print(varianza(data1))
print(np.var(data2))
emisiones['CO2 (kt)'].var() #varianza con pandas

# DESVIACION ESTANDAR - Raiz Cuadrada de la varianza, promedio de que tanto se alejan los datos a la media

def desviacionEstandar(datos):
	return np.sqrt(varianza(datos))

print(desviacionEstandar(data1))

np.std(data1) #desviacion estandar en numpy

emisiones['CO2 (kt)'].std()
