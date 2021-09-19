from tkinter import *
from tkinter import ttk
from tkinter.font import Font

ventana=Tk()
notebook=ttk.Notebook(ventana)
notebook.pack(fill="both", expand="yes")
pes0=ttk.Frame(notebook)
pes1=ttk.Frame(notebook)
pes2=ttk.Frame(notebook)
pes3=ttk.Frame(notebook)
pes4=ttk.Frame(notebook)
pes5=ttk.Frame(notebook)
notebook.add(pes0, text="MENU DEL DIA")
notebook.add(pes1, text="COMBOS")
notebook.add(pes2, text="BEBIDAS")
notebook.add(pes3, text="RESERVA DE MESA")
notebook.add(pes4, text="INVENTARIO")
notebook.add(pes5, text="REGISTRO DE EMPLEADOS")

imagen=PhotoImage(file="hamburger.1.gif")
fondo=Label(pes0, image=imagen, height=180, width=235).place(x=100, y=110)
lbl1=Label(pes0, text="$12.000", font=("fonty", 16)).place(x=185,y=315)
boton=Checkbutton(pes0, text="HAMBURGUESA", font=("fonty", 18)).place(x=140,y=290)

imagen1=PhotoImage(file="perro.gif")
fondo=Label(pes0, image=imagen1, height=180, width=235).place(x=480, y=110)
lbl2=Label(pes0, text="$8.000", font=("fonty", 16)).place(x=570,y=315)
boton1=Checkbutton(pes0, text="PERRO CALIENTE", font=("fonty", 18)).place(x=515,y=290)

imagen2=PhotoImage(file="papas.gif")
fondo=Label(pes0, image=imagen2, height=175, width=235).place(x=855, y=110)
lbl3=Label(pes0, text="$3.000", font=("fonty", 16)).place(x=943,y=315)
boton2=Checkbutton(pes0, text="PAPAS FRITAS", font=("fonty", 18)).place(x=900,y=290)

imagen3=PhotoImage(file="pizza.gif")
fondo=Label(pes0, image=imagen3,height=180, width=235).place(x=1200, y=110)
lbl4=Label(pes0, text="$5.000", font=("fonty", 16)).place(x=1284,y=315)
boton3=Checkbutton(pes0, text="PIZZA", font=("fonty", 18)).place(x=1275,y=290)

imagen4=PhotoImage(file="empanadas2.gif")
fondo=Label(pes0, image=imagen4, height=180, width=235).place(x=1560, y=110)
lbl5=Label(pes0, text="$3.000", font=("fonty", 16)).place(x=1650,y=315)
boton4=Checkbutton(pes0, text="EMPANADAS", font=("fonty", 18)).place(x=1613,y=290)

imagen5=PhotoImage(file="arepa.gif")
fondo=Label(pes0, image=imagen5, height=180, width=235).place(x=480, y=365)
lbl6=Label(pes0, text="$7.000", font=("fonty", 16)).place(x=570,y=575)
boton5=Checkbutton(pes0, text="AREPA RELLENA", font=("fonty", 18)).place(x=515,y=549)

imagen6=PhotoImage(file="Sandwich.gif")
fondo=Label(pes0, image=imagen6, height=180, width=235).place(x=100, y=365)
lbl7=Label(pes0, text="$5.000", font=("fonty", 16)).place(x=180,y=572)
boton6=Checkbutton(pes0, text="SANDWICH", font=("fonty", 18)).place(x=150,y=550)

imagen7=PhotoImage(file="Asado.gif")
fondo=Label(pes0, image=imagen7, height=180, width=235).place(x=855, y=365)
lbl8=Label(pes0, text="$22.000", font=("fonty", 16)).place(x=943,y=572)
boton7=Checkbutton(pes0, text="POLLO ASADO", font=("fonty", 18)).place(x=900,y=549)

imagen8=PhotoImage(file="Broaster.gif")
fondo=Label(pes0, image=imagen8, height=180, width=235).place(x=1200,y=365)
lbl9=Label(pes0, text="$27.000", font=("fonty", 16)).place(x=1284,y=570)
boton8=Checkbutton(pes0, text="POLLO A LA BROASTER", font=("fonty", 18)).place(x=1210,y=548)

imagen9=PhotoImage(file="Sushi.gif")
fondo=Label(pes0, image=imagen9, height=180, width=235).place(x=1560,y=365)
lbl10=Label(pes0, text="$40.000", font=("fonty", 16)).place(x=1650,y=570)
boton9=Checkbutton(pes0, text="SUSHI", font=("fonty", 18)).place(x=1643,y=547)

imagen10=PhotoImage(file="Arroz.gif")
fondo=Label(pes0, image=imagen10, height=180, width=235).place(x=100, y=625)
lbl11=Label(pes0, text="$18.000", font=("fonty", 16)).place(x=180,y=833)
boton10=Checkbutton(pes0, text="ARROZ CON POLLO", font=("fonty", 18)).place(x=125,y=810)

imagen12=PhotoImage(file="Salchi.gif")
fondo=Label(pes0, image=imagen12, height=180, width=235).place(x=480, y=625)
lbl11=Label(pes0, text="$7.000", font=("fonty", 16)).place(x=560,y=830)
boton11=Checkbutton(pes0, text="SALCHIPAPA", font=("fonty", 18)).place(x=527,y=806)

imagen13=PhotoImage(file="Costillitas.gif")
fondo=Label(pes0, image=imagen13, height=180, width=235).place(x=855, y=625)
lbl11=Label(pes0, text="$15.000", font=("fonty", 16)).place(x=938,y=830)
boton12=Checkbutton(pes0, text="COSTILLITAS", font=("fonty", 18)).place(x=900,y=806)

imagen14=PhotoImage(file="Nachos.gif")
fondo=Label(pes0, image=imagen14, height=180, width=235).place(x=1200,y=625)
lbl9=Label(pes0, text="$11.000", font=("fonty", 16)).place(x=1284,y=830)
boton13=Checkbutton(pes0, text="NACHOS CON QUESO", font=("fonty", 18)).place(x=1215,y=806)

imagen15=PhotoImage(file="Tacos.gif")
fondo=Label(pes0, image=imagen15, height=180, width=235).place(x=1560,y=625)
lbl10=Label(pes0, text="$9.000", font=("fonty", 16)).place(x=1650,y=830)
boton14=Checkbutton(pes0, text="TACOS", font=("fonty", 18)).place(x=1640,y=806)




imagen42=PhotoImage(file="combo4.gif")
fondo=Label(pes1, image=imagen42, height=300, width=300).place(x=1460,y=300)
boton=Checkbutton(pes1, text="COMBO 4", font=("fonty",50)).place(x=1485,y=235)
lbl331=Label(pes1, text="$7.000", font=("fonty",25)).place(x=1570,y=635)
lbl332=Label(pes1, text="Salchipapa+Gaseosa", font=("fonty",25)).place(x=1495,y=600)

imagen43=PhotoImage(file="combo1.gif")
fondo=Label(pes1, image=imagen43, height=300, width=300).place(x=100,y=300)
boton=Checkbutton(pes1, text="COMBO 1", font=("fonty",50)).place(x=130,y=235)
lbl341=Label(pes1, text="$15.000", font=("fonty",25)).place(x=203,y=670)
lbl342=Label(pes1, text="Hamburguesa+Papas Fritas", font=("fonty",25)).place(x=98,y=603)
lbl3521=Label(pes1, text="+Gaseosa", font=("fonty",25)).place(x=195,y=637)

imagen46=PhotoImage(file="combo2.gif")
fondo=Label(pes1, image=imagen46, height=300, width=300).place(x=560,y=300)
boton=Checkbutton(pes1, text="COMBO 2", font=("fonty",50)).place(x=585,y=235)
lbl351=Label(pes1, text="$11.000", font=("fonty",25)).place(x=660,y=670)
lbl352=Label(pes1, text="Perro Caliente+Papas Fritas", font=("fonty",25)).place(x=558,y=603)
lbl3521=Label(pes1, text="+Gaseosa", font=("fonty",25)).place(x=655,y=637)

imagen47=PhotoImage(file="combo3.gif")
fondo=Label(pes1, image=imagen47, height=300, width=300).place(x=1000,y=300)
boton=Checkbutton(pes1, text="COMBO 3", font=("fonty",50)).place(x=1025,y=235)
lbl361=Label(pes1, text="33.000", font=("fonty",25)).place(x=1105,y=635)
lbl362=Label(pes1, text="Pizza+Gaseosa", font=("fonty",25)).place(x=1065,y=603)






lbl10=Label(pes2, text="JUGOS NATURALES", font=("fonty",50)).place(x=150,y=100)

imagen16=PhotoImage(file="jugo-de-maracuya.gif")
fondo=Label(pes2, image=imagen16, height=180, width=235).place(x=100, y=210)
boton=Checkbutton(pes2, text="JUGO DE MARACUYA", font=("fonty", 16)).place(x=130,y=392)
text=Label(pes2,text="$4.000",font=("fonty", 16)).place(x=190,y=418)

imagen17=PhotoImage(file="jugodelulo.gif")
fondo=Label(pes2, image=imagen17, height=180, width=235).place(x=430,y=210)
boton=Checkbutton(pes2, text="JUGO DE LULO", font=("fonty", 16)).place(x=480,y=392)
text1=Label(pes2,text="$4.000",font=("fonty", 16)).place(x=520,y=418)

imagen18=PhotoImage(file="colombiana.gif")
fondo=Label(pes2, image=imagen18, height=180, width=235).place(x=855,y=210)
boton=Checkbutton(pes2, text="COLOMBIANA", font=("fonty", 16)).place(x=910,y=392)
text2=Label(pes2,text="$2.000",font=("fonty", 16)).place(x=945,y=418)

imagen19=PhotoImage(file="pepsi.gif")
fondo=Label(pes2, image=imagen19, height=180, width=235).place(x=1150,y=210)
boton=Checkbutton(pes2, text="PEPSI", font=("fonty", 16)).place(x=1230,y=392)
text2=Label(pes2,text="$2.000",font=("fonty", 16)).place(x=1238,y=418)

imagen20=PhotoImage(file="aguila.gif")
fondo=Label(pes2, image=imagen20, height=180, width=235).place(x=1560,y=210)
boton=Checkbutton(pes2, text="AGUILA", font=("fonty", 16)).place(x=1640,y=392)
text3=Label(pes2,text="$3.000",font=("fonty", 16)).place(x=1655,y=418)

imagen21=PhotoImage(file="jugodemango.gif")
fondo=Label(pes2, image=imagen21, height=180, width=235).place(x=100,y=525)
boton=Checkbutton(pes2, text="JUGO DE MANGO", font=("fonty", 16)).place(x=135,y=708)
text4=Label(pes2,text="$4.000",font=("fonty", 16)).place(x=185,y=730)

lbl10=Label(pes2, text="GASEOSAS", font=("fonty",50)).place(x=995,y=100)

imagen22=PhotoImage(file="limonada.gif")
fondo=Label(pes2, image=imagen22, height=180, width=235).place(x=430,y=525)
boton=Checkbutton(pes2, text="LIMONADA NATURAL", font=("fonty", 16)).place(x=455,y=708)
text4=Label(pes2,text="$5.000",font=("fonty", 16)).place(x=515,y=730)

imagen23=PhotoImage(file="7.gif")
fondo=Label(pes2, image=imagen23, height=180, width=235).place(x=855,y=525)
boton=Checkbutton(pes2, text="7UP", font=("fonty", 16)).place(x=943,y=708)
text5=Label(pes2,text="$2.000",font=("fonty", 16)).place(x=944,y=730)

lbl10=Label(pes2, text="CERVEZAS", font=("fonty",50)).place(x=1550,y=100)

imagen24=PhotoImage(file="coca.gif")
fondo=Label(pes2, image=imagen24, height=180, width=235).place(x=1150,y=525)
boton=Checkbutton(pes2, text="COCA COLA", font=("fonty", 16)).place(x=1210,y=708)
text6=Label(pes2,text="$2.000",font=("fonty", 16)).place(x=1240,y=730)

imagen25=PhotoImage(file="club.gif")
fondo=Label(pes2, image=imagen25, height=180, width=235).place(x=1560,y=525)
boton=Checkbutton(pes2, text="CLUB COLOMBIA", font=("fonty", 16)).place(x=1600,y=708)
text6=Label(pes2,text="$3.000",font=("fonty", 16)).place(x=1650,y=730)






lbl=Label(pes3, text="Elija una mesa: ", font=("fonty", 25)).place(x=900,y=30)

imagen26=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen26, height=130, width=170).place(x=315, y=110)
boton15=Checkbutton(pes3, text="MESA 1", font=("fonty", 18)).place(x=325,y=245)
combobox=ttk.Combobox(pes3, width=5)
combobox.place(x=415,y=245)
combobox['values']=('1','2','3','4','5')

imagen27=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen27, height=130, width=170).place(x=750, y=110)
boton16=Checkbutton(pes3, text="MESA 2", font=("fonty", 18)).place(x=760,y=245)
combobox1=ttk.Combobox(pes3, width=5)
combobox1.place(x=850,y=245)
combobox1['values']=('1','2','3','4','5')

imagen28=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen28, height=130, width=170).place(x=1195, y=110)
boton17=Checkbutton(pes3, text="MESA 3", font=("fonty", 18)).place(x=1205,y=245)
combobox2=ttk.Combobox(pes3, width=5)
combobox2.place(x=1295,y=245)
combobox2['values']=('1','2','3','4','5')

imagen29=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen29, height=130, width=170).place(x=1640, y=110)
boton18=Checkbutton(pes3, text="MESA 4", font=("fonty", 18)).place(x=1650,y=245)
combobox3=ttk.Combobox(pes3, width=5)
combobox3.place(x=1740,y=245)
combobox3['values']=('1','2','3','4','5')



imagen30=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen30, height=130, width=170).place(x=100, y=310)
boton19=Checkbutton(pes3, text="MESA 5", font=("fonty", 18)).place(x=110,y=445)
combobox4=ttk.Combobox(pes3, width=5)
combobox4.place(x=200,y=445)
combobox4['values']=('1','2','3','4','5')

imagen31=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen31, height=130, width=170).place(x=530, y=310)
boton20=Checkbutton(pes3, text="MESA 6", font=("fonty", 18)).place(x=540,y=445)
combobox5=ttk.Combobox(pes3, width=5)
combobox5.place(x=630,y=445)
combobox5['values']=('1','2','3','4','5')

imagen32=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen32, height=130, width=170).place(x=975, y=310)
boton21=Checkbutton(pes3, text="MESA 7", font=("fonty", 18)).place(x=985,y=445)
combobox6=ttk.Combobox(pes3, width=5)
combobox6.place(x=1075,y=445)
combobox6['values']=('1','2','3','4','5')

imagen33=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen33, height=130, width=170).place(x=1420, y=310)
boton22=Checkbutton(pes3, text="MESA 8", font=("fonty", 18)).place(x=1430,y=445)
combobox7=ttk.Combobox(pes3, width=5)
combobox7.place(x=1520,y=445)
combobox7['values']=('1','2','3','4','5')



imagen34=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen34, height=130, width=170).place(x=315, y=510)
boton23=Checkbutton(pes3, text="MESA 9", font=("fonty", 18)).place(x=325,y=645)
combobox8=ttk.Combobox(pes3, width=5)
combobox8.place(x=415,y=645)
combobox8['values']=('1','2','3','4','5')

imagen35=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen35, height=130, width=170).place(x=750, y=510)
boton24=Checkbutton(pes3, text="MESA 10", font=("fonty", 18)).place(x=755,y=645)
combobox8=ttk.Combobox(pes3, width=5)
combobox8.place(x=855,y=645)
combobox8['values']=('1','2','3','4','5')

imagen36=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen36, height=130, width=170).place(x=1185, y=510)
boton25=Checkbutton(pes3, text="MESA 11", font=("fonty", 18)).place(x=1192,y=645)
combobox9=ttk.Combobox(pes3, width=5)
combobox9.place(x=1290,y=645)
combobox9['values']=('1','2','3','4','5')

imagen37=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen37, height=130, width=170).place(x=1640, y=510)
boton26=Checkbutton(pes3, text="MESA 12", font=("fonty", 18)).place(x=1647,y=645)
combobox10=ttk.Combobox(pes3, width=5)
combobox10.place(x=1745,y=645)
combobox10['values']=('1','2','3','4','5')


imagen38=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen38, height=130, width=170).place(x=100, y=680)
boton27=Checkbutton(pes3, text="MESA 13", font=("fonty", 18)).place(x=104,y=815)
combobox11=ttk.Combobox(pes3, width=5)
combobox11.place(x=205,y=815)
combobox11['values']=('1','2','3','4','5')

imagen39=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen39, height=130, width=170).place(x=530, y=680)
boton28=Checkbutton(pes3, text="MESA 14", font=("fonty", 18)).place(x=534,y=815)
combobox11=ttk.Combobox(pes3, width=5)
combobox11.place(x=635,y=815)
combobox11['values']=('1','2','3','4','5')

imagen40=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen40, height=130, width=170).place(x=975, y=680)
boton29=Checkbutton(pes3, text="MESA 15", font=("fonty", 18)).place(x=979,y=815)
combobox11=ttk.Combobox(pes3, width=5)
combobox11.place(x=1080,y=815)
combobox11['values']=('1','2','3','4','5')

imagen41=PhotoImage(file="reserva.gif")
fondo=Label(pes3, image=imagen41, height=130, width=170).place(x=1420, y=680)
boton30=Checkbutton(pes3, text="MESA 16", font=("fonty", 18)).place(x=1424,y=815)
combobox11=ttk.Combobox(pes3, width=5)
combobox11.place(x=1525,y=815)
combobox11['values']=('1','2','3','4','5')

ventana.geometry("3000x3000")
ventana.mainloop()
