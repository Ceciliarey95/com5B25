import tkinter as tk


def hacer_algo():
    print("Estoy haciendo algo desde el boton de la interfaz")
# Creamos la ventana principal con tk

ventana = tk.Tk()
ventana.title('Mi primera ventana en el info con Tkinter')
ventana.geometry("500x500") # Ancho x alto en píxeles

# etiqueta = tk.Label(ventana, text='Hola mundo!', font=("Arial", 20))
# etiqueta.pack()

boton = tk.Button(ventana, text='Hola mundo!', font=("Arial", 20), command=hacer_algo)
boton.pack()

ventana.mainloop()