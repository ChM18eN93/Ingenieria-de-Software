# Archivos- Reemplazar o añadir contenido
from io import open


# Reemplazar contenido

notas = {
    "Nora": 87,
    "Gino": 100,
    "Loretto": 67,
    "Talina": 45
}
with open("frases_famosas.txt", "w") as archivo:
    for nombre, nota in notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")

# Añadir contenido

nuevas_notas = {
    "Laura": 87,
    "Julieta": 100,
    "Florencia": 67,
    "Ana": 45
}
with open("frases_famosas.txt", "a") as archivo:
    for nombre, nota in nuevas_notas.items():
        archivo.write(nombre + " - " + str(nota) + "\n")
