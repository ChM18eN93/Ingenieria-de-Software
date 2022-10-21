def primo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True

def numero_top(numero):
    numero_cadena = str(numero)
    suma_de_cifras = 0
    cantidad_cifras = len(numero_cadena)
    
    for cifra in numero_cadena:
        suma_de_cifras += int(cifra)
    
    resultado = suma_de_cifras / cantidad_cifras
    
    if primo(numero):
        return True
    return False

# Prueba

numero = int(input("ingrese un numero: "))

resultado= numero_top(numero)

if resultado:
    print("SI es Top")
else:
    print("NO es Top")

