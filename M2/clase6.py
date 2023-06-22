import pandas as pd
import numpy as np

# 02-06-2023


venta = pd.read_csv('venta.csv')
print('Venta: \n', venta.columns)

canal = pd.read_csv('CanalDeVenta.csv')
print('\nCanal: \n', canal)

producto = pd.read_csv('Producto.csv', encoding = 'ISO-8859-1')
print('\nProducto: \n', producto)


