# Clase 1 - Martes 2/05/2023

# Homework : Crear una función capaz de convertir números enteros de base 10
# a base 2. Debe recibir como parámetro el número a convertir


# def aBinario(numero):
#     if numero < 0:
#         print('Debe ingresar un número mayor que cero')
#         return None
#     if numero == 0:
#         return numero
#     if type(numero) != int:
#         print('Debe ingresar un número entero')
#         return None
#     else:
#         ''' Creamos una lista vacia para ir guardando los valores '''
#         lista_binaria = []
#         ''' Definimos el primer binario del numero ingresado '''
#         modulo = numero%2
#         lista_binaria.append(modulo)
#         ''' Definimos una lista vacia para los cocientes '''
#         lista_cocientes = []
#         cociente = numero // 2
#         lista_cocientes.append(cociente)
        
#         for i in lista_cocientes:
#             if i == 1:
#                 break
#             else:
#                 nuevo_cociente = i//2
#                 lista_cocientes.append(nuevo_cociente)
#         ''' Ahora ya que tenemos la lista de cocientes, vamos a crear la lista binaria '''
#         for i in lista_cocientes:
            
#             if i == 1:
#                 lista_binaria.append(1)
#             else:
#                 binario = i%2
#                 lista_binaria.append(binario)

#         ''' Ahora chequeamos que el valor que hayamos introducido coincida con la
#             lista binaria creada '''
#         lista_binaria_invertida = lista_binaria[::-1]
#         contador = len(lista_binaria)
#         numero_entero = 0
#         j = 0
#         for i in lista_binaria_invertida:
#             longitud_de_lista = len(lista_binaria)
#             contador -= 1
#             if i == 1:
#                 j = 2
#                 numero_entero += j**(contador)
#             else:
#                 j = 0        
                    
#         print('Lista de cocientes: \n')
#         print (lista_cocientes)
#         print('Lista de binarios: \n')
#         print (lista_binaria[::-1])
#         print('Valor calculado a partir de la lista binaria: \n')
#         return(numero_entero)


def numeroBinario(numero):
	# listaBinaria = []
	# resultado = ''	si no usara una lista esto seria otra forma

	if not isinstance(numero, int) or numero < 0:
		return None

	posicion = 0
	resultado = 0

	while numero > 0:
		resto = numero % 2
		numero = numero // 2
		# listaBinaria.append(resto)
		# resultado = resultado + str(resto) esta es la otra forma
		
		resultado += resto * pow(10, posicion)
		posicion += 1

	return resultado

# print(aBinario(29))
print(numeroBinario(29))


# Solo aplica a numeros menores a 1
def decimalABinario(numero):
	resultado = '0.'
	digitos = 10

	while numero > 0 and digitos > 0:

		numero = numero * 2
		entero = int(numero)
		decimal = numero % 1
		resultado += str(entero)
		numero = decimal
		digitos -= 1
	
	return resultado 

for i in range(2, 9):
	print('1/', i, ': ', decimalABinario(1/i))
