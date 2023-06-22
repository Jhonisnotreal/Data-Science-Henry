# 7/06/2023

import pymysql
import pandas as pd
from datetime import datetime

df = pd.read_csv('./dataset_viajes_sube.csv')

# print(df.info())
# print(df.head())

df = df.loc[df['CANTIDAD'].notna()]
# print(df.info())

df = df.rename(str.lower, axis='columns').reset_index(drop=True)
# print(df.head())

def fechas(df):
	lista = df['dia'].to_list()
	fechas = []
	
	for i in range(len(lista)):
		dia = lista[i][:2]
		mes = lista[i][2:5]
		anio = lista[i][5:9]
		fecha = anio + '-' + mes + '-' + dia
		fecha = datetime.strptime(fecha, '%Y-%b-%d')
		fechas.append(fecha)
	
	df['dia'] = fechas
	return df

# print(df['dia'][0])
print(fechas(df))

# ---- CREANDO TABLA CON TIPOS DE TRANSPORTE
tipo_transporte = pd.DataFrame(columns = ['idTransporte', 'nombreTransporte'])

for idx, val in enumerate(df['tipo_transporte'].unique(), start = 1):
	tipo_transporte.loc[idx] = [idx, val]
	# print(idx, val)

print(tipo_transporte)

# ORDENAR DF TRANSPORTE POR FECHA

df = df.sort_values('dia').reset_index(drop=True)
# print(df)

print(df['parcial'].value_counts())

datos_subte = df.loc[df['tipo_transporte'] == 'Subte']
datos_tren = df.loc[df['tipo_transporte'] == 'Tren']
datos_colectivo = df.loc[df['tipo_transporte'] == 'Colectivo']

print(datos_colectivo)

columnas = ['dia', 'tipo_transporte', 'parcial', 'cantidad']
datos_subte = datos_subte[columnas]
datos_colectivo = datos_colectivo[columnas]
datos_tren = datos_tren[columnas]

# print(datos_colectivo)

datos_subte['tipo_transporte'] = tipo_transporte['idTransporte'].loc[tipo_transporte['nombreTransporte'] == 'Subte'].values[0]
# print(datos_subte)

datos_colectivo['tipo_transporte'] = tipo_transporte['idTransporte'].loc[tipo_transporte['nombreTransporte'] == 'Colectivo'].values[0]
datos_tren['tipo_transporte'] = tipo_transporte['idTransporte'].loc[tipo_transporte['nombreTransporte'] == 'Tren'].values[0]

print(datos_subte)

# CONEXION A LA DB
conexion = pymysql.connect(
	host = 'localhost',
	user = 'root',
	password = 'Aftrpython19'
)

cursor = conexion.cursor()
crear_db = 'create database if not exists transporte;'
# cursor.execute(crear_db)

cursor.execute('use transporte')

create_tipo = '''
create table if not exists tipo_transporte(
idTransporte int not null auto_increment primary key,
nombreTransporte varchar(50)
)
'''

cursor.execute(create_tipo)
conexion.commit()


create_subte = '''
create table if not exists subte(
idSubte int not null auto_increment primary key,
fecha date,
tipoTransporte int,
parcial boolean,
cantidad float,
foreign key (tipoTransporte) references tipo_transporte(idTransporte)
)
'''

cursor.execute(create_subte)
conexion.commit()

create_tren = '''

create table if not exists tren(
idTren int not null auto_increment primary key,
fecha date,
tipoTransporte int,
parcial boolean,
cantidad float,
foreign key (tipoTransporte) references tipo_transporte(idTransporte)
)

'''

create_colectivo = '''

create table if not exists colectivo(
idColectivo int not null auto_increment primary key,
fecha date,
tipoTransporte int,
parcial boolean,
cantidad float,
foreign key (tipoTransporte) references tipo_transporte(idTransporte)
)

'''

cursor.execute(create_tren)
cursor.execute(create_colectivo)


# CARGAR DATOS DEL DF EN LA DB

filas_tipo = [tuple(tipo_transporte.iloc[i].values) for i in range(tipo_transporte.shape[0])]
# print('\n', filas_tipo)

fill_transporte = '''
insert into tipo_transporte (idTransporte, nombreTransporte)
values (%s, %s)
'''

# cursor.executemany(fill_transporte, filas_tipo)
conexion.commit()

insert_subte = '''
insert into subte (fecha, tipoTransporte, parcial, cantidad)
values (%s, %s, %s, %s)
'''

filas_subte = [tuple(datos_subte.iloc[i].values) for i in range(datos_subte.shape[0])]

cursor.executemany(insert_subte, filas_subte)


insert_tren = '''
insert into tren (fecha, tipoTransporte, parcial, cantidad)
values (%s, %s, %s, %s)
'''

filas_tren = [tuple(datos_tren.iloc[i].values) for i in range(datos_tren.shape[0])]

cursor.executemany(insert_tren, filas_tren)

insert_colectivo = '''
insert into colectivo (fecha, tipoTransporte, parcial, cantidad)
values (%s, %s, %s, %s)
'''

filas_colectivo = [tuple(datos_colectivo.iloc[i].values) for i in range(datos_colectivo.shape[0])]

cursor.executemany(insert_colectivo, filas_colectivo)

conexion.commit()

# TRAYENDO LOS DATOS
# cursor.execute('select * from subte limit 3;')
query = '''
select subte.fecha, tipo_transporte.nombreTransporte, subte.cantidad 
from subte 
join tipo_transporte 
on tipo_transporte.idTransporte = subte.tipoTransporte
limit 10;
'''
cursor.execute(query)

for i in cursor:
	print(i)

new_df = pd.DataFrame(columns=['fecha', 'tipoTransporte', 'cantidad'])

for i, val in enumerate(cursor):
	new_df.loc[i] = val

print(new_df.info())


# CARGAR DATOS DE LAS TABLAS
