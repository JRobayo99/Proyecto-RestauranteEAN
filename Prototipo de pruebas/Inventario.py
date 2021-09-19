import tkinter as tk
from tkinter import*
from tkinter import messagebox

import pymysql


bd=pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db="inventario"    
    )

cursor = bd.cursor()

cursor.execute("CREATE TABLE Inventario(Nombre del producto int PRIMARY KEY AUTO_INCREMENT NOT NULL, nombre_p VARCHAR(50), cantidad_c VARCHAR(50), clasifc_p VARCHAR(50), precio_u VARCHAR(50) NOT NULL)")

vnt=tk.Tk()
vnt.title("Formulario de registro")
vnt.geometry("350x700")
vnt.configure(background="tomato")

image=tk.PhotoImage(file="logo1.gif")
image=image.subsample(3,3)
label=tk.Label(image=image)
label.pack()

e0=tk.Label(vnt,text="Nombre del producto", bg="gray",fg="white")
e0.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

ed0=tk.Entry(vnt)
ed0.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

e1=tk.Label(vnt,text="Cantidad del producto", bg="gray",fg="white")
e1.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

ed1=tk.Entry(vnt)
ed1.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

e2=tk.Label(vnt,text="Clasificación del producto", bg="gray",fg="white")
e2.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

ed2=tk.Entry(vnt)
ed2.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

e3=tk.Label(vnt,text="Precio por unidad", bg="gray",fg="white")
e3.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

ed3=tk.Entry(vnt)
ed3.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

boton0=tk.Button(vnt, text="Registar en \n inventario", fg="black")
boton0.place(x=50,y=500)

boton1=tk.Button(vnt, text="Actualizar el \n inventario", fg="black")
boton1.place(x=200,y=500)

boton2=tk.Button(vnt, text="Eliminar del \n inventario", fg="black")
boton2.place(x=50,y=600)

boton3=tk.Button(vnt, text="Consultar en \n inventario", fg="black")
boton3.place(x=200,y=600)

boton4=tk.Button(vnt, text="Salir", fg="black")
boton4.place(x=150,y=650)

vnt.mainloop()
