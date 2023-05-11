# Clase 2 - Miercoles 3/05/2023

'''
Datos - Informacion

Tipos de Datos

Datos Cuantitativos/Numericos, Datos Cualitativos (Categoricos), 
Datos ordinales (Primero, Segundo, Tercero)

Datos Cuantitativos - 
1) Discretos (Goles, Votos.) y 
2) Continuos (temperatura, precios, sueldos. Porque el valor cambia constantemente)
'''

# Datos Cuantitativos

precio_sandia = 29.5

# Datos Cualitativos : Categoricos

nacionalidad = 'argentino'

codigo_pais = {
	'Argentina': 1,
	'Paraguay': 2,
	'Colombia': 3,
}

# Datos Ordinales

nivelEstudios = 'Universidad'
nivelEstds = 'Secundario'

'''
Falencias en los datos

- Errores
- Valores Faltantes

Hay valores nulos?
Que datos son discretos y cuales continuos? 
Errores? Se pueden eliminar?
'''

# Homework
import os

archivo = open('Emisiones_CO2.csv', 'r', encoding = 'ANSI')
# print(archivo)

dicc_emisiones = {  'cod_pais' : [],
                    'nom_pais' : [],
                    'region' : [],
                    'anio' : [],
                    'co2' : [],
                    'co2_percapita' : []}

print(dicc_emisiones.keys())

for i in dicc_emisiones.keys():
	print(dicc_emisiones[i][100])

archivo.close()


# RETOMAS DESDE next(archivo) APROX
# MINUTO 10 - 20 DE LA GRABACION
