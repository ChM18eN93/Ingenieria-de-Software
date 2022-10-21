
class Auto:
    color = ''
    modelo = ''
    llantas = 0
    puertas = 0
    velocidades = 0
    # Definiendo método de inicialización (Constructor)
    def __init__(self, col, model, llant, puer, vel):
        self.color = col
        self.modelo = model
        self.llantas = llant
        self.puertas = puer
        self.velocidades = vel
    
    def mostrarDatos(self):
        print('Color: ', self.color)
        print('Modelo: ', self.modelo)
        print('Llantas: ', self.llantas)
        print('Puertas: ', self.puertas)
        print('Velocidades: ', self.velocidades)

# Creando objetos

cochecito = Auto('Azul', 'Mercedes Benz', 4, 4, 5)
cochecito2 = Auto('Rojo', 'BMW', 4, 2, 6)
cochecito3 = Auto('blanco', 'Audi', 4, 2, 3)
cochecito.mostrarDatos()
cochecito2.mostrarDatos()
cochecito3.mostrarDatos()        
