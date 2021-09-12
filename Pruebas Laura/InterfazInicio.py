from tkinter import *

ventana=Tk()
ventana.title("RESTAURANTE EAN")

lbl=Label(ventana, text="BIENVENIDOS", font=("fonty", 50)).place(x=805, y=80)
ventana.config(bg="dark green")

lbl=Label(ventana, text="Por favor elija una opcion:", font=("fonty", 35)).place(x=765,y=250)

imgBoton=PhotoImage(file="Bandeja.gif")
btnSaludar=Button(ventana, image=imgBoton, height=350, width=500).place(x=100, y=500)
lbl=Label(ventana, text="MENU", font=("fonty", 20)).place(x=325,y=472)

imgBoton1=PhotoImage(file="2.gif")
btnSaludar=Button(ventana, image=imgBoton1, height=350, width=500).place(x=700, y=500)
lbl=Label(ventana, text="EMPLEADOS", font=("fonty", 20)).place(x=900,y=472)

imgBoton2=PhotoImage(file="Mesa.gif")
btnSaludar=Button(ventana, image=imgBoton2, height=350, width=500).place(x=1300, y=500)
lbl=Label(ventana, text="RESERVAS", font=("fonty", 20)).place(x=1500,y=472)

ventana.mainloop()