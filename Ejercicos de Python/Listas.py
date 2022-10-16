# Listas

lista = ["a", 4, "H", "todo"]

print(lista[0])

print(lista[1])

print(lista[2])

print(lista[3])

# método append

lista.append(7)
print(lista)

# Método insert
lista.insert(2, "agua")
print(lista)

# Método remove
lista.remove(4)
print(lista)

Vocales = ["a", "e", "i", "o", "u"]

if "j" in Vocales:
    print("True")
elif "i" in Vocales:
    print("True")
else:
    print("False")

# Extrae un elemento de la lista y lo coloca en una variable
marca = "i" in Vocales
print(marca)

# Método index - Muestra el contenido de un ídice
print(Vocales.index("e"))

# Método index 

lista = ["a", "b", 10, "todo"]

print(lista)

# Si quiero saber la posición de un elemento de la lista
print(lista.index(10))

# Si quiero saber el contenido de un índice de la lista

print(lista[2])

# para eliminar el último elemento de una lista

lista.pop()

print(lista)

# Para invertir el orden de una lista
lista.reverse()

print(lista)

# Para ordenar el contenido de una lista

lista = [ 1, 4, 2, 18, 5]

print(lista)
lista.sort()
print(lista)

lista = ["b", "a", "c", "b"]
print(lista)
lista.sort()
print(lista)

# Para saber cuántos elementos tiene una lista

print(lista)
print(lista.count("b"))

# Para agregar elementos de otra lista a una lista

lista1 = [1, 2, 3, 4]
print(lista1)

lista2 = [8, 9, 10]
print(lista2)

lista1.append(lista2)
print(lista1)
