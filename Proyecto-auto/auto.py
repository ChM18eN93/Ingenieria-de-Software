class Auto:
    color = ''
    modelo = ''
    llantas = ''
    puertas = 0
    velocidades = 0
    
# Creando métodos
# Sintaxis
# def nombre_Metodo(self)
#       acciones

    def mostrarDatos(self):
        print('Color: ', self.color)
        print('modelo: ', self.modelo)
        print('llantas: ', self.llantas)
        print('puertas: ', self.puertas)
        print('velocidades: ', self.velocidades)
        
# Aquí asignamos los valores

cochecito = Auto()
cochecito.color = 'Azul'
cochecito.modelo = 'Mercedes Benz'
cochecito.llantas = 4
cochecito.puertas = 2
cochecito.velocidades = 5
cochecito.mostrarDatos()

