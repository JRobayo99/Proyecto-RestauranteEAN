from tkinter import *
from tkinter import ttk
from tkinter.font import Font

ventana=Tk()
notebook=ttk.Notebook(ventana)
notebook.pack(fill="both", expand="yes")
pes0=ttk.Frame(notebook)
pes1=ttk.Frame(notebook)
pes2=ttk.Frame(notebook)
notebook.add(pes0, text="COMIDA")
notebook.add(pes1, text="BEBIDAS")
notebook.add(pes2, text="COMBOS")

imagen=PhotoImage(file="hamburger.1.gif")
fondo=Label(pes0, image=imagen, height=180, width=235).place(x=100, y=110)
lbl1=Label(pes0, text="$12.000", font=("fonty", 16)).place(x=185,y=295)

imagen1=PhotoImage(file="perro.gif")
fondo=Label(pes0, image=imagen1, height=180, width=235).place(x=480, y=110)
lbl2=Label(pes0, text="$8.000", font=("fonty", 16)).place(x=570,y=295)

imagen2=PhotoImage(file="papas.gif")
fondo=Label(pes0, image=imagen2, height=175, width=235).place(x=855, y=110)
lbl3=Label(pes0, text="$3.000", font=("fonty", 16)).place(x=943,y=290)

imagen3=PhotoImage(file="pizza.gif")
fondo=Label(pes0, image=imagen3,height=180, width=235).place(x=1200, y=110)
lbl4=Label(pes0, text="$5.000", font=("fonty", 16)).place(x=1284,y=295)

imagen4=PhotoImage(file="empanadas2.gif")
fondo=Label(pes0, image=imagen4, height=180, width=235).place(x=1560, y=110)
lbl5=Label(pes0, text="$3.000", font=("fonty", 16)).place(x=1650,y=295)

imagen5=PhotoImage(file="arepa.gif")
fondo=Label(pes0, image=imagen5, height=180, width=235).place(x=480, y=365)
lbl6=Label(pes0, text="$7.000", font=("fonty", 16)).place(x=570,y=551)

imagen6=PhotoImage(file="Sandwich.gif")
fondo=Label(pes0, image=imagen6, height=180, width=235).place(x=100, y=365)
lbl7=Label(pes0, text="$5.000", font=("fonty", 16)).place(x=180,y=552)

imagen7=PhotoImage(file="Asado.gif")
fondo=Label(pes0, image=imagen7, height=180, width=235).place(x=855, y=365)
lbl8=Label(pes0, text="$22.000", font=("fonty", 16)).place(x=943,y=551)

imagen8=PhotoImage(file="Broaster.gif")
fondo=Label(pes0, image=imagen8, height=180, width=235).place(x=1200,y=365)
lbl9=Label(pes0, text="$27.000", font=("fonty", 16)).place(x=1284,y=551)

imagen9=PhotoImage(file="Sushi.gif")
fondo=Label(pes0, image=imagen9, height=180, width=235).place(x=1560,y=365)
lbl10=Label(pes0, text="$40.000", font=("fonty", 16)).place(x=1650,y=550)

imagen10=PhotoImage(file="Arroz.gif")
fondo=Label(pes0, image=imagen10, height=180, width=235).place(x=100, y=625)
lbl11=Label(pes0, text="$18.000", font=("fonty", 16)).place(x=180,y=812)

imagen12=PhotoImage(file="Salchi.gif")
fondo=Label(pes0, image=imagen12, height=180, width=235).place(x=480, y=625)
lbl11=Label(pes0, text="$7.000", font=("fonty", 16)).place(x=560,y=810)

imagen13=PhotoImage(file="Costillitas.gif")
fondo=Label(pes0, image=imagen13, height=180, width=235).place(x=855, y=625)
lbl11=Label(pes0, text="$15.000", font=("fonty", 16)).place(x=938,y=810)

imagen14=PhotoImage(file="Nachos.gif")
fondo=Label(pes0, image=imagen14, height=180, width=235).place(x=1200,y=625)
lbl9=Label(pes0, text="$11.000", font=("fonty", 16)).place(x=1284,y=810)

imagen15=PhotoImage(file="Tacos.gif")
fondo=Label(pes0, image=imagen15, height=180, width=235).place(x=1560,y=625)
lbl10=Label(pes0, text="$9.000", font=("fonty", 16)).place(x=1650,y=810)

lbl10=Label(pes1, text="JUGOS NATURALES", font=("fonty",50)).place(x=10,y=10)

ventana.geometry("3000x3000")
ventana.mainloop()