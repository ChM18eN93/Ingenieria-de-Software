
import time

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
        
    # Métodos encender y apagar
    def encender(self):
        print('El auto encendió')
        
    def apagar(self):
        print('El auto se apagó')
        
    def acelerar(self, velocidad):
        for i in range(0, velocidad,2):
            print('El auto está acelerando a una velocidad de: ', i, 'Km/h')
            time.sleep(0.5)
        print('El auto llegó a la Velocidad de: ', velocidad, 'Km/h')
        
        
    def frenar(self, velocidad, frenado):
        for i in range(velocidad, frenado, -2):
            print('El auto está frenando, el odómetro marca: ', i, 'Km/h')
            time.sleep(0.5)
        print('El auto bajó a la velocidad de: ', frenado, 'Km/h')
            
                       
# Aquí asignamos los valores

cochecito = Auto()
cochecito.color = 'Azul'
cochecito.modelo = 'Mercedes Benz'
cochecito.llantas = 4
cochecito.puertas = 2
cochecito.velocidades = 5
cochecito.mostrarDatos()
cochecito.encender()
cochecito.acelerar(120)
cochecito.frenar(120, 60)
cochecito.apagar()


