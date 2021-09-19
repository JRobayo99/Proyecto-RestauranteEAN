import tkinter as tk

vnt=tk.Tk()
vnt.title("Formulario de registro")
vnt.geometry("500x700")
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

