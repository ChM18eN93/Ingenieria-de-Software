# Errores y excepciones

x = 5

if x > 15:
    print("Mayor que 15")
else:
    print("Menor que 15")

# Excepción
# Estructura completa
#try:
#    intenta ejecutar código
#except:
#    Si ocurre una excepción se detiene
#    y ejecuta el except
# else:
#     Si no ocurrió la excepción 'try'
#     ejecuta este código
# finally:
#      luego, ejecuta sí o sí este código


num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

try:
    resultado = num1 /num2
    print(f"{num1} / {num2} = ", resultado)
except:
    print("alerta, Excepción")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

try:
    resultado = num1 /num2
    print(f"{num1} / {num2} = ", resultado)
except ZeroDivisionError:
    print("alerta, Excepción2")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

try:
    resultado = num1 /num2
    print(f"{num1} / {num2} = ", resultado)
except ZeroDivisionError as e:
    print(e)

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

try:
    resultado = num1 /num2
    print(f"{num1} / {num2} = ", resultado)
except ZeroDivisionError as e:
    print(e)
else:
    print("Else")


num3 = int(input("Ingrese un número: "))
num4 = int(input("Ingrese otro número: "))

try:
    resultado = num3 /num4
    print(f"{num3} / {num4} = ", resultado)
except ZeroDivisionError as e:
    print(e)
finally:
    print("Finaly")