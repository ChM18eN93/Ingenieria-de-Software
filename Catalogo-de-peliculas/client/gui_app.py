from sre_parse import State
import tkinter as tk
#Aquí se crea la barra de menú horizontal
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)
# Aquíse crean los submenúes    
    menu_inicio.add_command(label ='Crear Registro en DB')
    menu_inicio.add_command(label ='Eliminar registro en DB')
    menu_inicio.add_command(label ='Salir', command = root.destroy)
# Aquí se crea el resto de los menúes    
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')

# Aquí se crea una clase Frame, donde irán
# todos los elementos de la pantalla

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg = 'blue')

        self.campos_pelicula()
        self.deshabilitar_campos()
# Método de la clase Frame
    def campos_pelicula(self):
        # Lbel de cada objeto
        self.label_nombre = tk.Label(self, text = '´Nombre: ')
        self.label_nombre.config(font = ('Arial', 12, 'bold'))
        self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10 )
        
        self.label_duracion = tk.Label(self, text = 'Duración: ')
        self.label_duracion.config(font = ('Arial', 12, 'bold'))
        self.label_duracion.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.label_genero = tk.Label(self, text = 'Género: ')
        self.label_genero.config(font = ('Arial', 12, 'bold'))
        self.label_genero.grid(row = 2, column = 0, padx = 10, pady = 10)
        
        # Entrada de datos
        
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width = 50, font = ('Arial', 12))
        self.entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan=2)        

        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width = 50, font = ('Arial', 12))
        self.entry_duracion.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan=2)

        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width = 50, font = ('Arial', 12))
        self.entry_genero.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan=2)    

        # Botones
        self.boton_nuevo = tk.Button(self, text='Nuevo')
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg = '#DAD5D6', bg = '#158645', cursor = 'hand2', activebackground = '#358D6F')
        self.boton_nuevo.grid(row = 4, column = 0, padx = 10, pady = 10)
        
        self.boton_guardar = tk.Button(self, text='Guardar')
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg = '#DAD5D6', bg = '#1658A2', cursor = 'hand2', activebackground = '#3586DF')
        self.boton_guardar.grid(row = 4, column = 1, padx = 10, pady = 10)
        
        self.boton_cancelar = tk.Button(self, text='Cancelar')
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg = '#DAD5D6', bg = '#BD152E', cursor = 'hand2', activebackground = '#E15370')
        self.boton_cancelar.grid(row = 4, column = 2, padx = 10, pady = 10)
        
    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
            
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')
        
    def deshabilitar_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
            
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')