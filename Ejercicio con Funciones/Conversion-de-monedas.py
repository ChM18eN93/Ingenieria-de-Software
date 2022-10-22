

def menu():
    print('1. Dolar')
    print('2. Dolar Canadiense')
    print('3. Euro')
    print('4. Libra Esterlina')
    print('5. Centenario')
    print('Cuánto tienes en pesos mexicanos? ')
    global pesos
    pesos = input()
    pesos = float(pesos)
    print('Qué tipo de cambio desea realizar ')
    global cambio
    cambio = input()
    cambio = int(cambio)
    
    # Evaluando tipo de cambio
    if (cambio ==1):
        print('Cuál es el precio del Dolar el día de hoy?')
        global predioD
        precioD = input()
        precioD = float(precioD)
        global dinerito
        dinerito = pesos/precioD
        print('Tienes ', dinerito, 'Dolares')

# Llamando a la función menu

menu()

    