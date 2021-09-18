import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql

def menu_pantalla():
    global pantalla
    pantalla =Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenido")
    pantalla.iconbitmap("logo1.ico")
    pantalla.configure(bg="saddle brown")


    image=PhotoImage(file="logo1.gif")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label(text="Acceso al sistema", bg="navy", fg="white", width="300", height="3",font=("Calibri",15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesión", height="3",width="30",command= inicio_sesion).pack()
    Label(text="").pack()

    Button(text="Registrar usuario", height="3",width="30",command=registrar).pack()

    pantalla.mainloop()


def inicio_sesion():
    global pantalla1
    pantalla1= Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio Sesion")
    pantalla1.iconbitmap("logo1.ico")

    Label(pantalla1, text="Por favor ingrese su Usario y Contraseña\n",bg="navy", fg="white", width="300", height="3",font=("Calibri",15)).pack()
    Label(pantalla1, text="").pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry = Entry(pantalla1, textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar Sesión").pack()

def registrar():
    global pantalla2
    pantalla2= Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registro Usuario")
    pantalla2.iconbitmap("logo1.ico")

    global nombreusuario_entry
    global contraseña_entry

    nombreusuario_entry=StringVar()
    contraseña_entry=StringVar()

    Label(pantalla2, text="Por favor ingrese un nombre de usuarioy una contraseña ",bg="navy", fg="white", width="300", height="3",font=("Calibri",15)).pack()
    Label(pantalla2, text="").pack()

    Label(pantalla2, text="Usuario").pack
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña").pack
    contraseña_entry = Entry(pantalla2)
    contraseña_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrar")
    
menu_pantalla().pack







