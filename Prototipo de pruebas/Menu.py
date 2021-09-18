from tkinter import *

ventana=Tk()

ventana.title("RESTAURANTE EAN")

ventana.geometry("3000x3000")
ventana.config(bg="dark green")

lbl=Label(ventana, text="Elija su menu:", font=("fonty", 25)).place(x=900,y=70)

frame=Frame(ventana)
frame.pack()

imagen=PhotoImage(file="hamburger.1.gif")
fondo=Label(ventana, image=imagen, height=180, width=235).place(x=100, y=150)
lbl=Label(ventana, text="HAMBURGUESA", font=("fonty", 18)).place(x=140,y=330)
lbl1=Label(ventana, text="$7.000", font=("fonty", 16)).place(x=175,y=350)

imagen1=PhotoImage(file="perro.gif")
fondo=Label(ventana, image=imagen1, height=180, width=235).place(x=480, y=150)
lbl=Label(ventana, text="PERRO CALIENTE", font=("fonty", 18)).place(x=525,y=330)
lbl2=Label(ventana, text="$5.000", font=("fonty", 16)).place(x=570,y=350)

imagen2=PhotoImage(file="papas.gif")
fondo=Label(ventana, image=imagen2, height=175, width=235).place(x=855, y=150)
lbl=Label(ventana, text="PAPAS FRITAS", font=("fonty", 18)).place(x=910,y=329)
lbl3=Label(ventana, text="$3.000", font=("fonty", 16)).place(x=943,y=350)

imagen3=PhotoImage(file="pizza.gif")
fondo=Label(ventana, image=imagen3,height=180, width=235).place(x=1200, y=150)
lbl=Label(ventana, text="PIZZA", font=("fonty", 18)).place(x=1285,y=330)
lbl4=Label(ventana, text="$6.000", font=("fonty", 16)).place(x=1284,y=350)

imagen4=PhotoImage(file="empanadas2.gif")
fondo=Label(ventana, image=imagen4, height=180, width=235).place(x=1560, y=150)
lbl=Label(ventana, text="EMPANADAS", font=("fonty", 18)).place(x=1628,y=330)
lbl5=Label(ventana, text="$6.000", font=("fonty", 16)).place(x=1650,y=350)

imagen5=PhotoImage(file="arepa.gif")
fondo=Label(ventana, image=imagen5, height=180, width=235).place(x=480, y=410)
lbl=Label(ventana, text="AREPA RELLENA", font=("fonty", 18)).place(x=525,y=593)
lbl6=Label(ventana, text="$5.000", font=("fonty", 16)).place(x=570,y=620)

imagen6=PhotoImage(file="Sandwich.gif")
fondo=Label(ventana, image=imagen6, height=180, width=235).place(x=100, y=410)
lbl=Label(ventana, text="SANDWICH", font=("fonty", 18)).place(x=160,y=593)
lbl7=Label(ventana, text="$12.000", font=("fonty", 16)).place(x=180,y=620)

imagen7=PhotoImage(file="Asado.gif")
fondo=Label(ventana, image=imagen7, height=180, width=235).place(x=855, y=410)
lbl=Label(ventana, text="POLLO ASADO", font=("fonty", 18)).place(x=910,y=590)
lbl8=Label(ventana, text="$20.000", font=("fonty", 16)).place(x=943,y=615)

imagen8=PhotoImage(file="Broaster.gif")
fondo=Label(ventana, image=imagen8, height=180, width=235).place(x=1200,y=410)
lbl=Label(ventana, text="POLLO A LA BROASTER", font=("fonty", 18)).place(x=1220,y=593)
lbl9=Label(ventana, text="$27.000", font=("fonty", 16)).place(x=1284,y=615)

imagen9=PhotoImage(file="Sushi.gif")
fondo=Label(ventana, image=imagen9, height=180, width=235).place(x=1560,y=410)
lbl=Label(ventana, text="SUSHI", font=("fonty", 18)).place(x=1653,y=590)
lbl10=Label(ventana, text="$17.000", font=("fonty", 16)).place(x=1650,y=615)

imagen10=PhotoImage(file="Arroz.gif")
fondo=Label(ventana, image=imagen10, height=180, width=235).place(x=100, y=680)
lbl=Label(ventana, text="ARROZ CON POLLO", font=("fonty", 18)).place(x=135,y=865)
lbl11=Label(ventana, text="$12.000", font=("fonty", 16)).place(x=180,y=890)

imagen12=PhotoImage(file="Salchi.gif")
fondo=Label(ventana, image=imagen12, height=180, width=235).place(x=480, y=680)
lbl=Label(ventana, text="SALCHIPAPA", font=("fonty", 18)).place(x=537,y=863)
lbl11=Label(ventana, text="$12.000", font=("fonty", 16)).place(x=560,y=890)

imagen13=PhotoImage(file="Costillitas.gif")
fondo=Label(ventana, image=imagen13, height=180, width=235).place(x=855, y=680)
lbl=Label(ventana, text="COSTILLITAS", font=("fonty", 18)).place(x=910,y=863)
lbl11=Label(ventana, text="$12.000", font=("fonty", 16)).place(x=938,y=890)

imagen14=PhotoImage(file="Nachos.gif")
fondo=Label(ventana, image=imagen14, height=180, width=235).place(x=1200,y=680)
lbl=Label(ventana, text="NACHOS CON QUESO", font=("fonty", 18)).place(x=1225,y=863)
lbl9=Label(ventana, text="$27.000", font=("fonty", 16)).place(x=1284,y=890)

imagen15=PhotoImage(file="Tacos.gif")
fondo=Label(ventana, image=imagen15, height=180, width=235).place(x=1560,y=680)
lbl=Label(ventana, text="TACOS", font=("fonty", 18)).place(x=1650,y=863)
lbl10=Label(ventana, text="$17.000", font=("fonty", 16)).place(x=1650,y=890)

scrollbar = Scrollbar(ventana)
scrollbar.pack(side=RIGHT, fill=Y)

ventana.mainloop()