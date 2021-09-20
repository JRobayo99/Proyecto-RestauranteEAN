from tkinter import *

ventana=Tk()

ventana.title("RESTAURANTE EAN")

ventana.geometry("700x600")
ventana.config(bg="dark green")

lbl=Label(ventana, text="Elija su menu:", font=("fonty", 25)).place(x=900,y=70)

frame=Frame(ventana)
frame.pack()

imagen=PhotoImage(file="Hamburguesa.gif")
fondo=Label(ventana, image=imagen, height=350, width=500).place(x=100, y=150)
lbl=Label(ventana, text="HAMBURGUESA", font=("fonty", 20)).place(x=290,y=155)
lbl1=Label(ventana, text="$", font=("fonty", 20)).place(x=100,y=500)
Checkbutton(frame="Hamburguesa").place(x=0, y=0)

imagen1=PhotoImage(file="perro.gif")
fondo=Label(ventana, image=imagen1, height=350, width=500).place(x=700, y=150)
lbl=Label(ventana, text="PERRO CALIENTE", font=("fonty", 20)).place(x=890,y=155)
lbl2=Label(ventana, text="$", font=("fonty", 20)).place(x=700,y=500)

imagen2=PhotoImage(file="papas.gif")
fondo=Label(ventana, image=imagen2, height=350, width=500).place(x=1300, y=150)
lbl=Label(ventana, text="PAPAS FRITAS", font=("fonty", 20)).place(x=1500,y=150)
lbl3=Label(ventana, text="$", font=("fonty", 20)).place(x=1300,y=500)

ventana.mainloop()
