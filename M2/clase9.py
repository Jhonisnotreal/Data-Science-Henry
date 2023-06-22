# 9/06/2023

import pymysql
import pandas as pd

df = pd.read_csv('oferta_gastronomica.csv')
# print(df)

# print(df.columns)

columnas = ['id', 'nombre', 'categoria','direccion_completa', 'barrio', 'comuna']
df = df[columnas]


# df = df.dropna()

# print(df)



conexion = pymysql.connect(
	host = 'localhost',
	user = 'root',
	password = 'Aftrpython19'
)

cursor = conexion.cursor()

create_db = 'create database if not exists locales;'
cursor.execute(create_db)
conexion.commit()

cursor.execute('use locales;')

crear_tabla = '''
create table if not exists oferta_gastronomica( 
	id int not null primary key,
	nombre varchar(50),
	categoria varchar(50),
	direccion varchar(50),
	barrio varchar(50),
	comuna varchar(50)
)
'''

cursor.execute(crear_tabla)

tuplas = [tuple(df.iloc[i].values) for i in range(df.shape[0])] #recorre desde 0 hasta el numero de filas que tenga mi tabla


# print(df.shape[1])

# INSERTANDO DATOS


insertar_datos = '''
insert into oferta_gastronomica (id, nombre, categoria, direccion, barrio, comuna)
values (%s, %s, %s, %s, %s, %s);
'''

# cursor.executemany(insertar_datos, tuplas)
conexion.commit()

df.fillna('No hay datos disponibles')


cantidad_pubs = '''
select barrio, count(id) from oferta_gastronomica
where categoria = 'PUB'
group by barrio 
order by count(id) desc
limit 1;
'''

cursor.execute(cantidad_pubs)
barrio_con_mas_pubs = cursor.fetchall()
barrio_con_mas_pubs[0][0]

cantidad_locales_categoria = '''
select categoria, count(id) from oferta_gastronomica
group by categoria
order by count(id) desc;
'''

cursor.execute(cantidad_locales_categoria)
conexion.commit()

cantidad_por_categ = cursor.fetchall()
print(cantidad_por_categ)

restaurantes_por_comuna = '''
select comuna, count(id) from oferta_gastronomica
where categoria = 'RESTAURANTE'
group by comuna
order by comuna;
'''

cursor.execute(restaurantes_por_comuna)
rest_por_comuna = cursor.fetchall()
print(rest_por_comuna)