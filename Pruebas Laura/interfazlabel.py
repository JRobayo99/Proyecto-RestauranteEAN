"""
from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="restaurante.gif")

miLabel=Label(miFrame,text="Hola, Bienvenidos al Restaurante EAN", fg="dark green", font=("Arial", 18))

miLabel.place(x=100, y=200)

root.mainloop()

"""

from tkinter import *

root=Tk()

miFrame=Frame(root, width=1000, height=1000)

miFrame.pack()

miImagen=PhotoImage(file="restaurante.gif")

Label(miFrame, image=miImagen).place(x=0, y=0)

root.mainloop()
