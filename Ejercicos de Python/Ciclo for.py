# Ciclo for for i in range(inicio, fin)

for i in range(4):
    print(i)

# for con iterables

lista = ["l", "i", "s","t", "a"]

for i in lista:
    print(i)

# for con diccionarios

letras = {"a": 1, "b": 2}

for clave in letras:
    print(clave)

# for con valores del diccionario

for valor in letras.values():
    print(valor)

# Para iterar con clave y valor

for clave, valor in letras.items():
    print(clave, valor)
