import tkinter as tk

app = tk.Tk()
mensaje = """Hola a todos
me gusta
que aprendan sobre Python"""
lblMensaje = tk.Label(app, text= mensaje, fg='blue', justify = tk.RIGHT).pack()

lblmensaje2 = tk.Label(app, text=mensaje, fg='red', font='Helvetica 40 bold').pack()

lblmensaje3 = tk.Label(app, text='Ve los videos', fg='white', bg='red', font='Times 24 italic').pack()
app.mainloop()

