import tkinter as tk
from tkinter import *
from PIL import Image, ImageChops, ImageEnhance, ImageOps


app = tk.Tk()

logo = tk.PhotoImage(file='C:/Users/YO/Desktop/Ingenieria-de-Software/horizonte-informatico-y-grulla-azulJPG2.png')


#lblMensaje = tk.Label(app, image=logo).pack()

mensaje=""" Ahora colocamos
texto con una imagen
y experimentamos como
van a lucir junto
"""


#lblMensaje2 = tk.Label(app, image=logo).pack(side='left')
#lblMensaje3 = tk.Label(app, text=mensaje, width=300).pack(side='right')
msgMensaje = tk.Message(app, text=mensaje, width=300)
msgMensaje.config(bg='blue', fg='white', font='times 24 bold')
msgMensaje.pack()
#msgMensaje = tk.Label(app, text=mensaje, image=logo, compound=tk.CENTER).pack()

app.mainloop()