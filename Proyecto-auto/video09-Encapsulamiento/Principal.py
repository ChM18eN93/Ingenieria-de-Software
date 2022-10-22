from ModuloPersona import *

personita = Persona('Jorge')
personita = Persona('Genio')
personita.mostrarDatos()
personita.setContrasenia('12345')
personita.mostrarDatos()
# Obteniendo la contrasenia encapsulada
print('Contraseña: ', personita.getContrasenia())



