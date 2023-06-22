import pandas as pd
import numpy as np

# ESPACIOS MUESTRALES Y SUCESOS (O EVENTOS)

# CLASIFICACION DE LOS SUCESOS

ventas_d = {
	"Nacional": [24,19,7],
	"Importado": [6,15, 9]
}

df = pd.DataFrame(ventas_d, index=['Menos de 40', 'Entre 40 y 50', 'Mas de 50'])
print(df)

# En ventas_d hay 2**6 = 64 eventos: El evento nulo (imposible como un auto que sea a la vez nacional e importado), el evento
# Simple y c/u de eventos con tres, cuatro y cinco puntos muestrales
# Eventos - subconjuntos del espacio muestral

'''
Muestral = {A, B, C}
Eventos = {0, {A}, {B}, {C}, {A,B}, {A, C}, {B, C}, Muestral} = 2^3
'''

# 		SUCESOS (EVENTOS) EXCLUYENTES

# son eventos que no pueden suceder al mismo tiempo. P.e. un auto es nacional o es importado
# pero solo puede ser una de esas opciones

# SUCESOS COMPATIBLES - tienen un elemento en comun como esto:
'''
B = {2,4,6}
C = {2}

B n C = {2}
'''

# 		UNION - elementos que por lo menos esta en uno de los 2

# pares en un dado A = {2,4,6}
# no. mayores a 3  B = {4,5,6}

# A u B = {2,4,5,6}

# 		INTERSECCION - conjunto de todos los elementos que pertenecen tanto a A como a B
# pares en un dado A = {2,4,6}
# no. mayores a 3  B = {4,5,6}

# A n B = {4,6}

# Para entender Union e Interseccion busca "Diagramas de Venv"

# 		LEY DE LA ADICION

# P(A U B) = P(A) + P(B)
# P(A U B) = P(A) + P(B) - P(A n B)


# 		PROBABILIDAD CONDICIONAL

#  Que ocurra un evento B dado que ocurre otro evento A. P(B|A)

# P(A|B) = P(A n B) / P(B)


# 		SUCESOS INDEPENDIENTES
# Si 2 sucesos son independientes, la ocurrencia de uno no afecta la probabilidad del otr

# P(A|B) = P(A)


