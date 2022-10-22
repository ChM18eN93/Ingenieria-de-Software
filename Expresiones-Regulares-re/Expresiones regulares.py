import re; #Se importa el modulo 
cadena = input("Ingrese la cadena: ")
#Ingresamos una cadena 
patron = ("w+$") 
#Esta es una expresión regular que 
# nos va a permitir validar la cadena
if (re.match(patron,cadena)):
    
#La función re.match recibe 2 parámetros 
# un patrón a validar y una cadena
    print("Cadena valida!!")

else:
    print("Cadena no valida !!")