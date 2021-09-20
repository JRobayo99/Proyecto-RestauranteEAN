import tkinter as tk
from tkinter import*
from tkinter import messagebox

import pymysql


#cursor.execute("CREATE TABLE Lista(id int PRIMARY KEY AUTO_INCREMENT NOT NULL, nombre_p VARCHAR(50), cantidad_c VARCHAR(50), clasifc_p VARCHAR(50), precio_u VARCHAR(50) NOT NULL)")

def inserar_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="inventario"
        )

    cursor = bd.cursor()

    sql="INSERT INTO Lista(id, nombre_p,cantidad_c,clasifc_p,precio_u)\
          VALUES (NOT NULL,'{0}','{1}','{2}','{3}')".format(nomb.get(),cap.get(),cla.get(),preu.get())
    try:
         
        cursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro llevado con exito", title="Aviso")
    except:
         
        bd.rollback()
        messagebox.showinfo(message="Registro no  se llevo acabo", title="Aviso")
        
        bd.close()

def actualizar():
    bd= pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="inventario"
        )
    cursor = bd.cursor()
    
    sql = "UPDATE Lista SET cantidad_c='"+cap.get()+"',clasifc_p='"+cla.get()+"',precio_u='"+preu.get()+"' WHERE nombre_p='"+nomb.get()+"'"
    try:
        cursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Actualizacion exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No Actualizado",title="Aviso")

        bd.close 
        
def eliminar():
    bd= pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="inventario"
        )
    cursor = bd.cursor()
    sql = "DELETE FROM Lista WHERE nombre_p='"+nomb.get()+"'"
    try:
        cursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Borrado exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No Eliminado",title="Aviso")

        bd.close



def cerrar():
    vnt.destroy()

vnt=tk.Tk()
vnt.title("Formulario de registro")
vnt.geometry("350x700")
vnt.configure(background="tomato")

image=tk.PhotoImage(file="logo1.gif")
image=image.subsample(3,3)
label=tk.Label(image=image)
label.pack()

e=tk.Label(vnt,text="Id Producto", bg="gray",fg="white")
e.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

ed=tk.Entry(vnt)
ed.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

e0=tk.Label(vnt,text="Nombre del producto", bg="gray",fg="white")
e0.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

nomb=tk.Entry(vnt)
nomb.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

e1=tk.Label(vnt,text="Cantidad del producto", bg="gray",fg="white")
e1.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

cap=tk.Entry(vnt)
cap.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

e2=tk.Label(vnt,text="Clasificación del producto", bg="gray",fg="white")
e2.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

cla=tk.Entry(vnt)
cla.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

e3=tk.Label(vnt,text="Precio por unidad", bg="gray",fg="white")
e3.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

preu=tk.Entry(vnt)
preu.pack(padx=5, pady=5, ipadx=5, fill=tk.X)

boton0=tk.Button(vnt, text="Registar inventario", fg="black",command= inserar_datos)
boton0.place(x=50,y=550)

boton1=tk.Button(vnt, text="Actualizar inventario", fg="black", command= actualizar)
boton1.place(x=200,y=550)

boton2=tk.Button(vnt, text="Eliminar del  inventario", fg="black",command= eliminar)
boton2.place(x=50,y=600)

boton3=tk.Button(vnt, text="Consultar inventario", fg="black")
boton3.place(x=200,y=600)

boton4=tk.Button(vnt, text="Salir", fg="black",command = cerrar)
boton4.place(x=150,y=650)

vnt.mainloop()
