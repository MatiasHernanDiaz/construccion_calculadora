"""
Calculadora funcional
"""
try:
    import Tkinter as tk
except ModuleNotFoundError:
    import tkinter as tk




#----------------------------------------Funciones--------------------------------------------

def nun_display(num):
    #inserta numero
    display.insert(100,num) #posicciona el cursor en 100, me aseguro de que siempre este a la derecha

def simbolo_display(simbolo):
    #inserta simbolo visualmente
    return display.insert(100,simbolo)

def borrar():
    #borrar con C
    return display.delete(0, tk.END)

def igual():

    cadena = display.get()

    try:
        if "+" in cadena:
            if "." in cadena:
                lista_cadena = cadena.split("+")
                resultado = float(lista_cadena[0])+float(lista_cadena[1])
                display.delete(0, tk.END)
                display.insert(0,str(resultado))
            else:
                lista_cadena = cadena.split("+")
                resultado = int(lista_cadena[0]) + int(lista_cadena[1])
                display.delete(0, tk.END)
                display.insert(0, str(resultado))

        if "-" in cadena:
            if "." in cadena:
                lista_cadena = cadena.split("-")
                resultado = float(lista_cadena[0]) - float(lista_cadena[1])
                display.delete(0, tk.END)
                display.insert(0,str(resultado))
            else:
                lista_cadena = cadena.split("-")
                resultado = int(lista_cadena[0]) - int(lista_cadena[1])
                display.delete(0, tk.END)
                display.insert(0, str(resultado))

        if "x" in cadena:
            if "." in cadena:
                lista_cadena = cadena.split("x")
                resultado = float(lista_cadena[0]) * float(lista_cadena[1])
                display.delete(0, tk.END)
                display.insert(0,str(resultado))
            else:
                lista_cadena = cadena.split("x")
                resultado = int(lista_cadena[0]) * int(lista_cadena[1])
                display.delete(0, tk.END)
                display.insert(0, str(resultado))

        if "/" in cadena:
            try:
                lista_cadena = cadena.split("/")
                resultado = float(lista_cadena[0]) / float(lista_cadena[1])
                display.delete(0, tk.END)
                display.insert(0, str(resultado))
            except:
                display.delete(0, tk.END)
                display.insert(0, "### ERROR DIV CERO")
    except:
        display.delete(0, tk.END)
        display.insert(0, "### ERROR ###")

#-----------------------------------------Ventana----------------------------------------------

root = tk.Tk()
root.title("CALCULADORA")
root.config(bg = "#aaffff")
#root.resizable(False, False) deshabilitar modificar ventana

#---------------------------------------ICONO-----------------------------------------------------
try:
    root.iconbitmap('calculadora_icono.ico')
except:
    pass


#-------------------------------------Frame para display--------------------------------------

frame_display = tk.Frame(root)
frame_display.grid(row = 0, column = 0)
frame_display.config(bg = "#aaffff")



#----------------------------------Frame para botones----------------------------------------

frame_boton = tk.Frame(root)
frame_boton.grid(row = 1, column = 0)
frame_boton.config(bg = "#aaffff", relief="solid", bd = "2")


#----------------------------------Frame botones operacion------------------------------------
"""
Agregar un frame para los botones de operacion. Desconfigura la interfas. averiguar!!
frame_operacion = tk.Frame(root)
frame_boton.grid(row = 0, column =1)
"""


#-------------------------------------Display-------------------------------------------------

display = tk.Entry(frame_display, justify="right")
display.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)
display.config(bg = "white", relief = "solid", bd = "2") #state="readonly"
display.focus_set() #hace foco en el display para que al iniciar me permita ingresar digitos por teclado sin tener que seleccionarlo



#-----------------------------------Botones de numeros-----------------------------------------

boton0 = tk.Button(frame_boton, text = "0", width = 3, height = 1, padx = 10, pady = 10, command = lambda: nun_display(0))
boton0.config(bg = "#fff")
boton0.grid(row = 5, column = 1)

boton1 = tk.Button(frame_boton, text = "1", width = 3, height = 1, padx = 10, pady = 10, command = lambda: nun_display(1))
boton1.config(bg = "#fff")
boton1.grid(row = 4, column = 0)

boton2 = tk.Button(frame_boton, text = "2", width = 3, height = 1, padx = 10, pady = 10, command = lambda: nun_display(2))
boton2.config(bg = "#fff")
boton2.grid(row = 4, column = 1)

boton3 = tk.Button(frame_boton, text = "3", width = 3, height = 1, padx = 10, pady = 10, command = lambda: nun_display(3))
boton3.config(bg = "#fff")
boton3.grid(row = 4, column = 2)

boton4 = tk.Button(frame_boton, text = "4", width = 3, height = 1, padx = 10, pady = 10, command = lambda: nun_display(4))
boton4.config(bg = "#fff")
boton4.grid(row = 3, column = 0)

boton5 = tk.Button(frame_boton, text = "5", width = 3, height = 1, padx = 10, pady = 10, command = lambda: nun_display(5))
boton5.config(bg = "#fff")
boton5.grid(row = 3, column = 1)

boton6 = tk.Button(frame_boton, text = "6", width = 3, height = 1, padx = 10, pady = 10, command = lambda: nun_display(6))
boton6.config(bg = "#fff")
boton6.grid(row = 3, column = 2)

boton7 = tk.Button(frame_boton, text = "7", width = 3, height = 1, padx = 10, pady = 10, command = lambda: nun_display(7))
boton7.config(bg = "#fff")
boton7.grid(row = 2, column = 0)

boton8 = tk.Button(frame_boton, text = "8", width = 3, height = 1, padx = 10, pady = 10, command = lambda: nun_display(8))
boton8.config(bg = "#fff")
boton8.grid(row = 2, column = 1)

boton9 = tk.Button(frame_boton, text = "9", width = 3, height = 1, padx = 10, pady = 10, command = lambda: nun_display(9))
boton9.config(bg = "#fff")
boton9.grid(row = 2, column = 2)


#---------------------------------------botones operacion-------------------------------------

boton_suma = tk.Button(frame_boton, text = "+", width = 3, height = 1, padx = 10, pady = 10, command = lambda: simbolo_display(" + "))
boton_suma.config(bg = "#fff")
boton_suma.grid( row = 2, column = 3)

boton_resta = tk.Button(frame_boton, text = "-", width = 3, height = 1, padx = 10, pady = 10, command = lambda: simbolo_display(" - "))
boton_resta.config(bg = "#fff")
boton_resta.grid( row = 3, column = 3)

boton_mul = tk.Button(frame_boton, text = "x", width = 3, height = 1, padx = 10, pady = 10, command = lambda: simbolo_display(" x "))
boton_mul.config(bg = "#fff")
boton_mul.grid( row = 4, column = 3)

boton_div = tk.Button(frame_boton, text = "/", width = 3, height = 1, padx = 10, pady = 10, command = lambda: simbolo_display(" / "))
boton_div.config(bg = "#fff")
boton_div.grid( row = 5, column = 3)

#se decide colocar el boton C en frame display, no queda escuadrado, averiguar

boton_borrar = tk.Button(frame_display, text = "C", width = 3, height = 1, padx = 10, pady = 10, command = borrar)
boton_borrar.config(bg = "#fff")
boton_borrar.grid( row = 1, column = 4)

boton_igual = tk.Button(frame_boton, text = "=", width = 3, height = 1, padx = 10, pady = 10, command = igual)
boton_igual.config(bg = "#fff")
boton_igual.grid( row = 5, column = 2)

boton_punto = tk.Button(frame_boton, text = ".", width = 3, height = 1, padx = 10, pady = 10, command = lambda: simbolo_display("."))
boton_punto.config(bg = "#fff")
boton_punto.grid( row = 5, column = 0)

root.mainloop()
