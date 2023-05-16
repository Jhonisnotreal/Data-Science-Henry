import pandas as pd
import numpy as np

df = pd.read_csv('Emisiones_CO2.csv', sep='|', decimal = ',', encoding='latin-1', thousands='.')

def hash_function(key):
    return sum(index * ord(character) for index, character in enumerate(repr(key), start=1))

df.dropna(inplace=True)
df['Clave_Hash'] = df['Código de país'].apply(hash_function)


# print(df.head)
# print(df.columns)
print("\n")
print(df.info())

# print(df.loc[df['CO2 (kt)'].isna()]) #Filas Vacias y columnas


print("\n")
print(hash_function('pato'))
print(hash_function('tapo'))
print(hash_function('gato'))
# print(df['Código de país'].unique())
print(df[['Código de país', 'Clave_Hash']])

# -----------------------------Ejercicio 2
df2 = pd.read_csv('Emisiones_CO2.csv', sep='|', decimal=',', encoding='latin-1')
df2.drop_duplicates()


print(df.columns)
tupla = ['Clave_Hash', 'Código de país', 'Nombre del país', 'Región']
df_pais = df[tupla].drop_duplicates()

print(df_pais)
tupla_2 = ['Año', 'CO2 (kt)', 'CO2 per ca[ita (toneladas metricas)', 'Clave_Hash']
df.drop(['Código de país', 'Nombre del país', 'Región'], axis = 1, inplace = True) #axis - columnas

# df_pais.loc(df_pais['Clave_Hash'].duplicated())

df_pais['Clave_Hash'].value_counts()

# df_pais.to_csv('df_pais.csv', index=False)
# df.to_csv('df.csv', index=False)




# -----------------------------Recurso Clase
#Enumerate le doy una [] y en val guardo el valor de cada elemento con indice i
# for i, val in enumerate(['A', 'B', 'C', 'D']):
#     print(i, val, ord(val))

# for i, val in enumerate('string', start = 1):
#     print(i, val)

# repr(1000000) #Transforma en string

# el ord() es el codigo ASCII

# inplace si es True la hace en el dataframe original, con False solo modifica cuando ejecuto el codigo sin
# modificar el dataframe original