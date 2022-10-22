class Persona:
    usuario = ''
    # Para encapsular, se utiliza doble guión bajo
    __contraseña = ''
    def __init__(self, user):
        self.usuario = user
    
    # Definiendo los métodos para manipular el encapsulamiento
    def setContrasenia(self, passw):
        self.__contraseña = passw
    def getContrasenia(self):
        return self.__contraseña
    def mostrarDatos(self):
        print('Usuario', self.usuario)
        print('Contrasenia', self.getContrasenia())
        
        
    