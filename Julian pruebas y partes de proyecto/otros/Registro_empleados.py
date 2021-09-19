import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
import datetime


def menu_pantalla():
    global pantalla
    pantalla =Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenido")
    pantalla.iconbitmap("logo1.ico")
    pantalla.configure(bg="gray")


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
    contrasena_usuario_entry = Entry(pantalla1,show="*", textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar Sesión", command=validacion_datos).pack()

def registrar():
    global pantalla2
    pantalla2= Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registro Usuario")
    pantalla2.iconbitmap("logo1.ico")

    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry=StringVar()
    contrasena_entry=StringVar()

    Label(pantalla2, text="Por favor ingrese un nombre de usuario y una contraseña \n ",bg="navy", fg="white", width="300", height="3",font=("Calibri",15)).pack()
    Label(pantalla2, text="").pack()

    Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña").pack()
    contrasena_entry = Entry(pantalla2,show="*")
    contrasena_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrar",command=inserta_datos).pack()

def inserta_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="empleados"
        )
    fcursor=bd.cursor()
    
    sql="INSERT INTO login (Usuario, Clave)VALUES('{0}','{1}')".format(nombreusuario_entry.get(),contrasena_entry.get())
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")

    except:
        bd.rollback()
        messagebox.showinfo(message="Registro no Exitoso ", title="Aviso")

    bd.close()
ahora= datetime.datetime.now()
def validacion_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="empleados"
        )
    fcursor=bd.cursor()
    
    fcursor.execute("SELECT Clave FROM login WHERE Usuario='"+nombreusuario_verify.get()+"'and Clave='"+contrasenausuario_verify.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo(title="inico de sesion correcto", message="Usuario y contraseña correcta")
        global pantalla3
        pantalla3 =tkinter.Toplevel()
        pantalla3.geometry("300x300")
        pantalla3.title("Registro de ingreso o salida")
        pantalla3.iconbitmap("logo1.ico")
        pantalla3.configure(bg="grey")

        
        def mensaje():
            
            messagebox.showinfo(title="Hora de entrada", message= ahora)

        def mensaje2():
            
            messagebox.showinfo(title="Hora de salida", message=ahora)

        
        lbltitulo=Label(pantalla3,text="Marque la entrada o salida",bg="navy", fg="white", width="300", height="3",font=("Calibri",15)).pack()
        boton= Button(pantalla3,text="Entrada",height="5",width="40",command=mensaje).place(x=6, y=80)
        boton= Button(pantalla3,text="Salida",height="5",width="40",command=mensaje2).place(x=6, y=200)
       
        
        
    else:
        messagebox.showinfo(title="inico de sesion incorrecto", message="Usuario o contraseña incorrectos")
    bd.close()
        
menu_pantalla()







