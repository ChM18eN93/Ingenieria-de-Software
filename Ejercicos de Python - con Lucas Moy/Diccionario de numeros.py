# Diccionario
numeros = {
    '1': 'UNO',
    '2' : 'DOS',
    '3' : 'TRES',
    '4': 'CUATRO',
    '5' : 'CINCO',
    '6' : 'SEIS',
    '7' : 'SIETE',
    '8': 'OCHO',
    '9' : 'NUEVE',
    '0' : 'DIEZ'}

texto =input('Ingrese un número: ')

textofinal = ''
for letra in texto:
    textofinal += numeros[letra] + ' '

print(textofinal)