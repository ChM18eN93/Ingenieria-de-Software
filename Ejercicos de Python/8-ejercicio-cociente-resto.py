n = int(input('Ingrese el primer número: '))
m = int(input('Ingrese el segundo número: '))

c = round(n / m, 2)
r = (n % m)

print('El dividendo es: ', n)
print('El divisor es: ', m)
print('El cociente es: ',c)
print('El resto es: ', r)