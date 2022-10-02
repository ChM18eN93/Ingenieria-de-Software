
from io import open
with open("frases_famosas.txt", "r") as archivo:
    for linea in archivo:
        print(linea)
