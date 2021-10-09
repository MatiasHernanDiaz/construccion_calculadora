"""
Intento de creacion de una Calculadora funcional
"""
try:
    import Tkinter as tk
except ModuleNotFoundError:
    import tkinter as tk

#parametros de la ventana
ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.resizable(False,False)

#parametros del contenedor
calculadora = tk.Frame(ventana)
calculadora.config(bg = "white")
calculadora.pack()


class num_boton:
    def __init__(self,num,row,column):
        #recibe 3 parametros, el numero, y la posicion como row y column
        self.num = num
        self.row = row
        self.column = column

        #configuracion del boton
        tk.Button(calculadora,bg = "white",
                  text=self.num,
                  width = 5, height = 3,
                  relief="raised", borderwidth=3,
                  command = lambda: print(self.num)).grid(padx = 1, pady = 1, row = self.row, column = self.column)





boton1 = num_boton(1,2,0)
boton2 = num_boton(2, 2, 1)
boton3 = num_boton(3,2,2)
boton4 = num_boton(4,1,0)
boton5 = num_boton(5,1,1)
boton6 = num_boton(6,1,2)
boton7 = num_boton(7,0,0)
boton8 = num_boton(8,0,1)
boton9 = num_boton(9,0,2)






ventana.mainloop()
