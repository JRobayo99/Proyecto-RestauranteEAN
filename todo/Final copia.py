from tkinter import *
from tkinter import ttk
from tkinter.font import Font

ventana=Tk()
notebook=ttk.Notebook(ventana)
notebook.pack(fill="both", expand="yes", )
pes0=ttk.Frame(notebook)
pes1=ttk.Frame(notebook)
pes2=ttk.Frame(notebook)
pes3=ttk.Frame(notebook)
pes4=ttk.Frame(notebook)
notebook.add(pes0, text="RESTAURANTE EAN")
notebook.add(pes1, text="MENU DEL DIA")
notebook.add(pes2, text="RESERVE SU MESA")
notebook.add(pes3, text="INVENTARIO")
notebook.add(pes4, text="REGISTRO DE EMPLEADOS")
lbl=Label(pes0, text="BIENVENIDOS AL RESTAURANTE EAN", font=("boink let", 70)).place(x=385, y=200)
lbl1=Label(pes0, text="ESCOJA UNA DE LAS PAGINAS DE LA PARTE SUPERIOR", font=("boink let", 50), fg="dark green").place(x=350, y=560)


lbl2=Label(pes1, text="Elija su menu:", font=("fonty", 25)).place(x=900,y=30)

imagen=PhotoImage(file="hamburger.1.gif")
fondo=Label(pes1, image=imagen, height=180, width=235).place(x=100, y=110)
lbl=Label(pes1, text="HAMBURGUESA", font=("fonty", 18)).place(x=150,y=290)
lbl1=Label(pes1, text="$7.000", font=("fonty", 16)).place(x=185,y=310)

imagen1=PhotoImage(file="perro.gif")
fondo=Label(pes1, image=imagen1, height=180, width=235).place(x=480, y=110)
lbl=Label(pes1, text="PERRO CALIENTE", font=("fonty", 18)).place(x=525,y=290)
lbl2=Label(pes1, text="$5.000", font=("fonty", 16)).place(x=570,y=310)

imagen2=PhotoImage(file="papas.gif")
fondo=Label(pes1, image=imagen2, height=175, width=235).place(x=855, y=110)
lbl=Label(pes1, text="PAPAS FRITAS", font=("fonty", 18)).place(x=910,y=290)
lbl3=Label(pes1, text="$3.000", font=("fonty", 16)).place(x=943,y=310)

imagen3=PhotoImage(file="pizza.gif")
fondo=Label(pes1, image=imagen3,height=180, width=235).place(x=1200, y=110)
lbl=Label(pes1, text="PIZZA", font=("fonty", 18)).place(x=1285,y=290)
lbl4=Label(pes1, text="$6.000", font=("fonty", 16)).place(x=1284,y=310)

imagen4=PhotoImage(file="empanadas2.gif")
fondo=Label(pes1, image=imagen4, height=180, width=235).place(x=1560, y=110)
lbl=Label(pes1, text="EMPANADAS", font=("fonty", 18)).place(x=1628,y=290)
lbl5=Label(pes1, text="$6.000", font=("fonty", 16)).place(x=1650,y=310)

imagen5=PhotoImage(file="arepa.gif")
fondo=Label(pes1, image=imagen5, height=180, width=235).place(x=480, y=365)
lbl=Label(pes1, text="AREPA RELLENA", font=("fonty", 18)).place(x=525,y=549)
lbl6=Label(pes1, text="$5.000", font=("fonty", 16)).place(x=570,y=570)

imagen6=PhotoImage(file="Sandwich.gif")
fondo=Label(pes1, image=imagen6, height=180, width=235).place(x=100, y=365)
lbl=Label(pes1, text="SANDWICH", font=("fonty", 18)).place(x=160,y=550)
lbl7=Label(pes1, text="$12.000", font=("fonty", 16)).place(x=180,y=570)

imagen7=PhotoImage(file="Asado.gif")
fondo=Label(pes1, image=imagen7, height=180, width=235).place(x=855, y=365)
lbl=Label(pes1, text="POLLO ASADO", font=("fonty", 18)).place(x=910,y=549)
lbl8=Label(pes1, text="$20.000", font=("fonty", 16)).place(x=943,y=570)

imagen8=PhotoImage(file="Broaster.gif")
fondo=Label(pes1, image=imagen8, height=180, width=235).place(x=1200,y=365)
lbl=Label(pes1, text="POLLO A LA BROASTER", font=("fonty", 18)).place(x=1220,y=548)
lbl9=Label(pes1, text="$27.000", font=("fonty", 16)).place(x=1284,y=570)

imagen9=PhotoImage(file="Sushi.gif")
fondo=Label(pes1, image=imagen9, height=180, width=235).place(x=1560,y=365)
lbl=Label(pes1, text="SUSHI", font=("fonty", 18)).place(x=1653,y=547)
lbl10=Label(pes1, text="$17.000", font=("fonty", 16)).place(x=1650,y=570)

imagen10=PhotoImage(file="Arroz.gif")
fondo=Label(pes1, image=imagen10, height=180, width=235).place(x=100, y=625)
lbl=Label(pes1, text="ARROZ CON POLLO", font=("fonty", 18)).place(x=135,y=810)
lbl11=Label(pes1, text="$12.000", font=("fonty", 16)).place(x=180,y=830)

imagen12=PhotoImage(file="Salchi.gif")
fondo=Label(pes1, image=imagen12, height=180, width=235).place(x=480, y=625)
lbl=Label(pes1, text="SALCHIPAPA", font=("fonty", 18)).place(x=537,y=806)
lbl11=Label(pes1, text="$12.000", font=("fonty", 16)).place(x=560,y=828)

imagen13=PhotoImage(file="Costillitas.gif")
fondo=Label(pes1, image=imagen13, height=180, width=235).place(x=855, y=625)
lbl=Label(pes1, text="COSTILLITAS", font=("fonty", 18)).place(x=910,y=806)
lbl11=Label(pes1, text="$12.000", font=("fonty", 16)).place(x=938,y=828)

imagen14=PhotoImage(file="Nachos.gif")
fondo=Label(pes1, image=imagen14, height=180, width=235).place(x=1200,y=625)
lbl=Label(pes1, text="NACHOS CON QUESO", font=("fonty", 18)).place(x=1225,y=806)
lbl9=Label(pes1, text="$27.000", font=("fonty", 16)).place(x=1284,y=828)

imagen15=PhotoImage(file="Tacos.gif")
fondo=Label(pes1, image=imagen15, height=180, width=235).place(x=1560,y=625)
lbl=Label(pes1, text="TACOS", font=("fonty", 18)).place(x=1650,y=806)
lbl10=Label(pes1, text="$17.000", font=("fonty", 16)).place(x=1650,y=828)

ventana.geometry("3000x3000")
ventana.mainloop()
