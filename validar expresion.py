from tkinter import *
import re

#---------------PATRON-----------------------------------

patron = patron=re.compile(r"^[A-Z]{1}\d{3}[a-z]+\W{3}$")

#--------------VENTANA--------------------------------

ventana = Tk()
ventana.title("validador de expresión")
ventana.geometry("1020x600")
ventana.config(bg="dark turquoise")

label1 = Label(ventana, text="BIENVENIDO!!", bg="dark turquoise", font=('Arial',25))
label1.place(x=400, y=80)

label2 = Label(ventana, text="Ingrese la expresión que desea validar: ", bg="dark turquoise", font=('Arial',16))
label2.place(x=30, y=210)

entry1 = Entry(ventana)
entry1.place(x=492, y=215)
entry1.config(width=35, justify="center", font="Arial, 15")

#-------------FUNCION PARA VALIDAR EXPRESION-------------------

mensaje = StringVar()

def validar_expresion():
    expresion = str(entry1.get())
    if patron.search(expresion) != None:
        return mensaje.set("La expresión ingresada es valida")
    else:
        return mensaje.set("La expresión ingresada no es valida")
        
#---------------BOTON VALIDAR Y MENSAJE----------------------------

validar = Button(ventana, text="Validar", command=validar_expresion)
validar.place(x=495, y=340)

resultado = Entry(ventana, textvariable=mensaje, fg="red", font=('Arial',16))
resultado.config(width=30, justify="center")
resultado.place(x=310, y=420)

ventana.mainloop()

