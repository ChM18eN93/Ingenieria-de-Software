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

class Moto:
    color = ''
    modelo = ''
    llantas = 0
    velocidades = 0
    
    def __init__(self, col, model, llant, vel):
        self.color = col
        self.modelo = model
        self.llantas = llant
        self.velocidades = vel
    
    def mostrarDatos(self):
        print('Color: ', self.color)
        print('Modelo: ', self.modelo)
        print('Llantas: ', self.llantas)
        print('Velocidades: ', self.velocidades)

class Carretilla:
    color = ''
    marca = ''
    llantas = 0

    def __init__(self, col, marc, llant):
        self.color = col
        self.marca = marc
        self.llantas = llant
    
    def mostrarDatos(self):
        print('Color: ', self.color)
        print('Marca: ', self.marca)
        print('Llantas: ', self.llantas)

    
    
    