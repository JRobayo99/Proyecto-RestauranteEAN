import tkinter 

ventana= tkinter.Tk()
ventana.title("zz")
"""
etiqueta = tkinter.Label(ventana,text="Hola cara de monda", bg="green")
etiqueta.pack(side= tkinter.LEFT)
etiqueta2 = tkinter.Label(ventana,text="Hola cara de monda", bg="blue")
etiqueta2.pack(fill= tkinter.X, expand=1)
etiqueta3 = tkinter.Label(ventana,text="Hola cara de monda", bg="blue")
etiqueta3.pack(fill= tkinter.BOTH, expand=True)
"""
#esto sive para el tamaño del boton  padx= 40, pady= 60
"""
def saludo(nombre):
    print("Holandas perros"+ nombre)
boton1=tkinter.Button(ventana, text= "solo es un boton",command= lambda: saludo
(" Python"))
boton1.pack()
"""
#font= "Arial 60"
"""
cajatexto=tkinter.Entry(ventana)
cajatexto.pack()
etiqueta= tkinter.Label(ventana)
etiqueta.pack()

def textodelacaja():
    txt= cajatexto.get()
    etiqueta["text"]= txt

bonotn1=tkinter.Button(ventana, text="click",command= textodelacaja)
bonotn1.pack()
"""
boton1=tkinter.Button(ventana, text = " boton1",width=3, height=3)
boton2=tkinter.Button(ventana, text = " boton2",width=3, height=5)
boton3=tkinter.Button(ventana, text = " boton3",width=5, height=5)

boton1.grid(row = 5, column = 0)
boton2.grid(row = 6000, column = 2)
boton3.grid(row = 4, column= 4,padx=5,pady=5)

ventana.mainloop()