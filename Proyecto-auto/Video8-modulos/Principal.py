# Importar archivo moduloVehiculos

from ModuloVehiculos import Auto, Moto, Carretilla

# Creando las instancias (objetos)

cochecito = Auto('Azul', 'Mercedes Benz', 4, 4, 5)
motito = Moto('Azul', 'Yamaha', 2, 3)
carretillita = Carretilla('Gris', 'Dowen', 1)
cochecito.mostrarDatos()
motito.mostrarDatos()
carretillita.mostrarDatos()
