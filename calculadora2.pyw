"""
Intento de creacion de una Calculadora funcional
"""
try:
    import Tkinter as tk
except ModuleNotFoundError:
    import tkinter as tk

#Ventana

root = tk.Tk()
root.title("CALCULADORA")
#root.resizable(False, False) deshabilitar modificar ventana

#Frame

calcu = tk.Frame(root)
calcu.pack()

display = tk.Entry(calcu)
display.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)
display.config(bg = "white") #state="readonly"

#Botones de numeros

boton0 = tk.Button(calcu, text = "0", width = 3, height = 1, padx = 10, pady = 10)
boton0.config(bg = "#fff")
boton0.grid(row = 5, column = 1)

boton1 = tk.Button(calcu, text = "1", width = 3, height = 1, padx = 10, pady = 10)
boton1.config(bg = "#fff")
boton1.grid(row = 4, column = 0)

boton2 = tk.Button(calcu, text = "2", width = 3, height = 1, padx = 10, pady = 10)
boton2.config(bg = "#fff")
boton2.grid(row = 4, column = 1)

boton3 = tk.Button(calcu, text = "3", width = 3, height = 1, padx = 10, pady = 10)
boton3.config(bg = "#fff")
boton3.grid(row = 4, column = 2)

boton4 = tk.Button(calcu, text = "4", width = 3, height = 1, padx = 10, pady = 10)
boton4.config(bg = "#fff")
boton4.grid(row = 3, column = 0)

boton5 = tk.Button(calcu, text = "5", width = 3, height = 1, padx = 10, pady = 10)
boton5.config(bg = "#fff")
boton5.grid(row = 3, column = 1)

boton6 = tk.Button(calcu, text = "6", width = 3, height = 1, padx = 10, pady = 10)
boton6.config(bg = "#fff")
boton6.grid(row = 3, column = 2)

boton7 = tk.Button(calcu, text = "7", width = 3, height = 1, padx = 10, pady = 10)
boton7.config(bg = "#fff")
boton7.grid(row = 2, column = 0)

boton8 = tk.Button(calcu, text = "8", width = 3, height = 1, padx = 10, pady = 10)
boton8.config(bg = "#fff")
boton8.grid(row = 2, column = 1)

boton9 = tk.Button(calcu, text = "9", width = 3, height = 1, padx = 10, pady = 10)
boton9.config(bg = "#fff")
boton9.grid(row = 2, column = 2)



root.mainloop()