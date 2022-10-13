import tkinter as tk
from client.gui_app import Frame, barra_menu
def main():
    root = tk.Tk()
    root.title('Catalogo de peliculas')
    root.iconbitmap('C:/Users/YO/Desktop/Ingenieria-de-Software/Catalogo-de-peliculas/img\icono.ico')
    root.resizable(0,0)
    
    barra_menu(root)
    
    app = Frame(root = root)
    
    root.mainloop()
    
if __name__ == '__main__':
    main()