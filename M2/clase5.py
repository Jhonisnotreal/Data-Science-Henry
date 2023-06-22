import pandas as pd
import numpy as np
import calendar

# 31-05-2023 
# Sistemas de Gestion de Bases de Datos

'''
Data Warehouse
'''
print(calendar.month(2023, 6))

num = 8
def adder(integer):
	global num
	print(num)
	num = 10
	print(num + integer)

print(adder(5))