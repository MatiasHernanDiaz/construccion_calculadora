"""
Calculadora funcional
"""
try:
    import Tkinter as tk
except ModuleNotFoundError:
    import tkinter as tk


#----------------------------------------Funciones--------------------------------------------
def nun_display(num):
    return display.insert(1,num) #el 1 permite que el cursor se pocicione despues de ingresar el numero





#-----------------------------------------Ventana----------------------------------------------

root = tk.Tk()
root.title("CALCULADORA")
#root.resizable(False, False) deshabilitar modificar ventana

#-------------------------------------Frame para display--------------------------------------

frame_display = tk.Frame(root)
frame_display.grid(row = 0, column = 0)



#----------------------------------Frame para botones----------------------------------------

frame_boton = tk.Frame(root)
frame_boton.grid(row = 1, column = 0)


#----------------------------------Frame botones operacion------------------------------------
"""
Agregar un frame para los botones de operacion. Desconfigura la interfas. averiguar!!
frame_operacion = tk.Frame(root)
frame_boton.grid(row = 0, column =1)
"""


#-------------------------------------Display-------------------------------------------------

display = tk.Entry(frame_display, justify="right")
display.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)
display.config(bg = "white") #state="readonly"
display.focus_set() #hace foco en el display para que al iniciar me permita ingresar digitos por teclado sin tener que seleccionarlo



#-----------------------------------Botones de numeros-----------------------------------------

boton0 = tk.Button(frame_boton, text = "0", width = 3, height = 1, padx = 10, pady = 10, command = lambda : nun_display(0))
boton0.config(bg = "#fff")
boton0.grid(row = 5, column = 1)

boton1 = tk.Button(frame_boton, text = "1", width = 3, height = 1, padx = 10, pady = 10, command = lambda : nun_display(1))
boton1.config(bg = "#fff")
boton1.grid(row = 4, column = 0)

boton2 = tk.Button(frame_boton, text = "2", width = 3, height = 1, padx = 10, pady = 10, command = lambda : nun_display(2))
boton2.config(bg = "#fff")
boton2.grid(row = 4, column = 1)

boton3 = tk.Button(frame_boton, text = "3", width = 3, height = 1, padx = 10, pady = 10, command = lambda : nun_display(3))
boton3.config(bg = "#fff")
boton3.grid(row = 4, column = 2)

boton4 = tk.Button(frame_boton, text = "4", width = 3, height = 1, padx = 10, pady = 10, command = lambda : nun_display(4))
boton4.config(bg = "#fff")
boton4.grid(row = 3, column = 0)

boton5 = tk.Button(frame_boton, text = "5", width = 3, height = 1, padx = 10, pady = 10, command = lambda : nun_display(5))
boton5.config(bg = "#fff")
boton5.grid(row = 3, column = 1)

boton6 = tk.Button(frame_boton, text = "6", width = 3, height = 1, padx = 10, pady = 10, command = lambda : nun_display(6))
boton6.config(bg = "#fff")
boton6.grid(row = 3, column = 2)

boton7 = tk.Button(frame_boton, text = "7", width = 3, height = 1, padx = 10, pady = 10, command = lambda : nun_display(7))
boton7.config(bg = "#fff")
boton7.grid(row = 2, column = 0)

boton8 = tk.Button(frame_boton, text = "8", width = 3, height = 1, padx = 10, pady = 10, command = lambda : nun_display(8))
boton8.config(bg = "#fff")
boton8.grid(row = 2, column = 1)

boton9 = tk.Button(frame_boton, text = "9", width = 3, height = 1, padx = 10, pady = 10, command = lambda : nun_display(9))
boton9.config(bg = "#fff")
boton9.grid(row = 2, column = 2)


#---------------------------------------botones operacion-------------------------------------

boton_suma = tk.Button(frame_boton, text = "+", width = 3, height = 1, padx = 10, pady = 10)
boton_suma.config(bg = "#fff")
boton_suma.grid( row = 2, column = 3)

boton_resta = tk.Button(frame_boton, text = "-", width = 3, height = 1, padx = 10, pady = 10)
boton_resta.config(bg = "#fff")
boton_resta.grid( row = 3, column = 3)

boton_mul = tk.Button(frame_boton, text = "x", width = 3, height = 1, padx = 10, pady = 10)
boton_mul.config(bg = "#fff")
boton_mul.grid( row = 4, column = 3)

boton_div = tk.Button(frame_boton, text = "/", width = 3, height = 1, padx = 10, pady = 10)
boton_div.config(bg = "#fff")
boton_div.grid( row = 5, column = 3)

#se decide colocar el boton C en frame display, no queda escuadrado, averiguar

boton_borrar = tk.Button(frame_display, text = "C", width = 3, height = 1, padx = 10, pady = 10)
boton_borrar.config(bg = "#fff")
boton_borrar.grid( row = 1, column = 4)



root.mainloop()
