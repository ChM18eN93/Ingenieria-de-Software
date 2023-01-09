n = int(input('Ingrese el primer número: '))
m = int(input('Ingrese el segundo número: '))

c = round(n / m, 2)
r = (n % m)

print('El DIVIDENDO es: ', n)
print('El DIVISOR es: ', m)
print('El COCIENTE es: ',c)
print('El RESTO es: ', r)