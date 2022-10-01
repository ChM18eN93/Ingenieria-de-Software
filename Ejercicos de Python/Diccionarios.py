# Diccionarios

# Ejemplo

diccio = { "a": 4, "b": 5}

print(diccio)

# Para accedera un valor del diccionario

print(diccio["a"])

# Para acceder a un valor con el método get

print(diccio.get("a"))

# Añadir una clave valor aldiccionario

diccio["c"] = 8

print(diccio)

# Modificar valor

diccio["b"] = 34
print(diccio)

# Para borrar un elemento clave-valor

del diccio["a"]
print(diccio)

diccio["h"] = 14
print(diccio)

# verifiación de existencia de un elemento 
# en eldiccionario, se hace a través de la clave

print("a" in diccio)
print("h" in diccio)