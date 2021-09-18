from tkinter import *

ventana=Tk()
ventana.title("RESTAURANTE EAN")

lbl=Label(ventana, text="RESTAURANTE EAN", bg="dark green", fg="white", font=("fonty", 100,)).place(x=500,y=0)

lbl=Label(ventana, text="BIENVENIDOS", bg="dark green", fg="white", font=("fonty", 50)).place(x=805, y=200)
ventana.config(bg="black")

lbl=Label(ventana, text="Por favor elija una opcion:", bg="dark green", fg="white", font=("fonty", 35)).place(x=765,y=300)

imgBoton=PhotoImage(file="Bandeja.gif")
btnSaludar=Button(ventana, image=imgBoton, bg="dark green", height=350, width=500).place(x=100, y=500)
lbl=Label(ventana, text="MENU", bg="dark green", fg="white", font=("fonty", 20)).place(x=325,y=472)

imgBoton1=PhotoImage(file="2.gif")
btnSaludar=Button(ventana, image=imgBoton1, height=350, width=500).place(x=700, y=500)
lbl=Label(ventana, text="EMPLEADOS", bg="dark green", fg="white", font=("fonty", 20)).place(x=900,y=472)

imgBoton2=PhotoImage(file="Mesa.gif")
btnSaludar=Button(ventana, image=imgBoton2, height=350, width=500).place(x=1300, y=500)
lbl=Label(ventana, text="RESERVAS", bg="dark green", fg="white", font=("fonty", 20)).place(x=1500,y=472)

ventana.mainloop()