# 19-06-2023

# De datos a conocimiento

# Numeros peridicos, por que 3 x 3.3333 da 1?

import mysql.connector

connection = mysql.connector.connect(user='root', password='Aftrpython19',
                              host='127.0.0.1',
                              database='henry_01')

import pandas as pd

# df = pd.read_csv('Homework_Resuelto/Productos.csv', sep=',')
df = pd.read_excel('Homework/CanalDeVenta.xlsx')
# df = df.fillna(' ')


cursor = connection.cursor()

for i,row in df.iterrows():
    sql = "INSERT INTO canalVenta VALUES (" + "%s,"*(len(row)-1) + "%s)"

    
    cursor.execute(sql, tuple(row))

connection.commit()

print('Todo correcto')

