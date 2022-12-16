import math
peso = int(input('por favor, ingrese su peso: '))
altura = float(input(' ingrese su altua en metros'))

imc= peso/pow(altura,2)

print('Su masa corporal es: ', imc)