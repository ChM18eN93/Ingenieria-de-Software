# Ejercicio5
# Crear una lista con distintos valores ingresados por teclado
# Terminar la lista cuando se ingrese la palabrqa fin

lista = []
i = 1

while i < 5:
    valor =input('Ingrese un valor: ')
    lista.append(valor)
    i = i+1

print(lista)
