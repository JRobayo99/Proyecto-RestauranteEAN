from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200,height=600)
miFrame.pack()

cuadroTexto=Entry(miFrame)
cuadroTexto.grid(row=0, column=1)

nombreLabel=Label(miFrame, text="Buscar:")
nombreLabel.grid(row=0, column=0)

raiz.mainloop()