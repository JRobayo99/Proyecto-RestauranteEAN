from tkinter import *

class Principal:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Restaurante EAN")
        Label(self.ventana,text="Bienvenidos al Restaurante EAN, por favor elija una opcion:").grid(row=0, column=1)

if __name__=="__main__":
    ventana=Tk()
    ventana.geometry("700x600+0+0")
    ventana.config(bg="dark green")
    aplicacion=Principal(ventana)
    
    raiz=Tk()
    imagenC=PhotoImage(file="comida.gif", width=140, height=100)
    lblImagen=Label(ventana,image=imagenC).place(x=100, y=50)
    imagenL=PhotoImage(file="clientes.gif", width=200, height=280)
    lblImagen=Label(ventana,image=imagenL).place(x=100, y=150)
    ventana.mainloop()