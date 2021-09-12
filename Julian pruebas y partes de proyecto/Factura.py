import tkinter as tk

ventana= tk.Tk()
ventana.title ("Restaurante ménu del día")
ventana.geometry("700*500")
ventana.configure(bg= "White")

cliente= tk.StringVar()
ruc=tk.StringVar()
producto1 = tk.StringVar()
producto2 = tk.StringVar()
producto3 = tk.StringVar()
producto4 = tk.StringVar()
producto5 = tk.StringVar()
producto6 = tk.StringVar()

cantidad1 = tk.StringVar()
cantidad2 = tk.StringVar()
cantidad3 = tk.StringVar()
cantidad4 = tk.StringVar()
cantidad5 = tk.StringVar()
cantidad6 = tk.StringVar()

precio1 = tk.StringVar()
precio2 = tk.StringVar()
precio3 = tk.StringVar()
precio4 = tk.StringVar()
precio5 = tk.StringVar()
precio6 = tk.StringVar()

resultado1 = tk.StringVar()
resultado2 = tk.StringVar()
resultado3 = tk.StringVar()
resultado4 = tk.StringVar()
resultado5 = tk.StringVar()
resultado6 = tk.StringVar()
resultadoT = tk.StringVar()
resultadoTIVA = tk.StringVar()
iva= tk.StringVar()
lista = [producto1, producto2, producto3, producto4, producto5, producto6, cantidad1, cantidad2, cantidad3, cantidad4,cantidad5, cantidad6]
compro= False
def digit():
    global compro
    for i in lista:
        if i.get().isdigit()**True:
            compro= True
def calcular():
    digit ()
    print (compro)
    if compro == True:

        resultado1.set(float(cantidad1.get())*float(precio1.get()))
        resultado2.set(float(cantidad2.get())*float(precio2.get()))
        resultado3.set(float(cantidad3.get())*float(precio3.get()))
        resultado4.set(float(cantidad4.get())*float(precio4.get()))
        resultado5.set(float(cantidad5.get())*float(precio5.get()))
        resultado6.set(float(cantidad6.get())*float(precio6.get()))
        resultadoT.set("Subtotal: "+str(float(resultado1.get())+float
        (resultado2.get())+float(resultado3.get())+float(resultado3.get())+float(resultado4.get())+float(resultado5.get())+float(resultado6.get())))
        iva.__set("Iva: "+str(0.12(float(resultado1.get())+float(resultado2.get())+float(resultado3.get())+float(resultado4.get())+float(resultado5.get())+float(resultado6.get()))))
        resultadoTIVA.set("Total: "+str(1.12*(float(resultado1.get())+float(resultado2.get())+float(resultado3.get())+float(resultado4.get())+float(resultado5.get())+float(resultado1.get()))))
def limpiar():
    cliente.set("")
    ruc.set("")
    producto1.set("")
    producto2.set("")
    producto3.set("")
    producto4.set("")
    producto5.set("")
    producto6.set("")

    cantidad1.set("")
    cantidad2.set("")
    cantidad3.set("")
    cantidad4.set("")
    cantidad5.set("")
    cantidad6.set("")

    precio1.set("")
    precio2.set("")
    precio3.set("")
    precio4.set("")
    precio5.set("")
    precio6.set("")

    resultado1.set("")
    resultado2.set("")
    resultado3.set("")
    resultado4.set("")
    resultado5.set("")
    resultado6.set("")
    resultadoT.set("")
    resultadoTIVA.set("")
    iva.set("")

tk.Label(text="FACTURA: )", bg="white").place(x=275,y=10)

tk.Label(text="Cliente: ", bg= "while").place()



    