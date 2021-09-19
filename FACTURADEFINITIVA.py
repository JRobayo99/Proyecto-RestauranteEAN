import tkinter as tk

ventana = tk.Tk()
ventana.title("RESTAURANTE(Todo lo que puedas comer)")
ventana.geometry("700x500")
ventana.configure(bg = "white")



#variables
cliente = tk.StringVar()
ruc = tk.StringVar()
producto1 = tk.StringVar()
producto2 = tk.StringVar()
producto3 = tk.StringVar()
producto4 = tk.StringVar()
producto5 = tk.StringVar()
producto6 = tk.StringVar()
producto7 = tk.StringVar()
producto8 = tk.StringVar()
producto9 = tk.StringVar()
producto10 = tk.StringVar()
producto11 = tk.StringVar()
producto12 = tk.StringVar()
producto13 = tk.StringVar()
producto14 = tk.StringVar()
producto15 = tk.StringVar()

cantidad1 = tk.StringVar()
cantidad2 = tk.StringVar()
cantidad3 = tk.StringVar()
cantidad4 = tk.StringVar()
cantidad5 = tk.StringVar()
cantidad6 = tk.StringVar()
cantidad7 = tk.StringVar()
cantidad8 = tk.StringVar()
cantidad9 = tk.StringVar()
cantidad10 = tk.StringVar()
cantidad11 = tk.StringVar()
cantidad12 = tk.StringVar()
cantidad13 = tk.StringVar()
cantidad14 = tk.StringVar()
cantidad15 = tk.StringVar()

precio1 = tk.StringVar()
precio2 = tk.StringVar()
precio3 = tk.StringVar()
precio4 = tk.StringVar()
precio5 = tk.StringVar()
precio6 = tk.StringVar()
precio7 = tk.StringVar()
precio8 = tk.StringVar()
precio9 = tk.StringVar()
precio10 = tk.StringVar()
precio11 = tk.StringVar()
precio12 = tk.StringVar()
precio13 = tk.StringVar()
precio14 = tk.StringVar()
precio15 = tk.StringVar()


resultado1 = tk.StringVar()
resultado2 = tk.StringVar()
resultado3 = tk.StringVar()
resultado4 = tk.StringVar()
resultado5 = tk.StringVar()
resultado6 = tk.StringVar()
resultado7 = tk.StringVar()
resultado8 = tk.StringVar()
resultado9 = tk.StringVar()
resultado10 = tk.StringVar()
resultado11 = tk.StringVar()
resultado12 = tk.StringVar()
resultado13 = tk.StringVar()
resultado14 = tk.StringVar()
resultado15 = tk.StringVar()
resultadoT = tk.StringVar()
resultadoTIVA = tk.StringVar()
iva = tk.StringVar()
lista = [producto1,producto2,producto3,producto4,producto5,producto6,producto7,producto8,producto9,producto10,producto11,producto12,producto13,producto14,producto15,precio1,precio2,precio3,precio4,precio5,precio6,precio7,precio8,precio9,precio10,precio11,precio12,precio13,precio14,precio15,cantidad1,cantidad2,cantidad3,cantidad4,cantidad5,cantidad6,cantidad7,cantidad8,cantidad9,cantidad10,cantidad11,cantidad12,cantidad13,cantidad14,cantidad15]
compro = False
#funciones
def digit ():
    global compro
    for i in lista:
        if i.get().isdigit() == True:
            compro = True
def calcular():
    digit ()
    print(compro)
    if compro == True:
        
        resultado1.set(float(cantidad1.get())*float(precio1.get()))
        resultado2.set(float(cantidad2.get())*float(precio2.get()))
        resultado3.set(float(cantidad3.get())*float(precio3.get()))
        resultado4.set(float(cantidad4.get())*float(precio4.get()))
        resultado5.set(float(cantidad5.get())*float(precio5.get()))
        resultado6.set(float(cantidad6.get())*float(precio6.get()))
        resultado7.set(float(cantidad7.get())*float(precio7.get()))
        resultado8.set(float(cantidad8.get())*float(precio8.get()))
        resultado9.set(float(cantidad9.get())*float(precio9.get()))
        resultado10.set(float(cantidad10.get())*float(precio10.get()))
        resultado11.set(float(cantidad11.get())*float(precio11.get()))
        resultado12.set(float(cantidad12.get())*float(precio12.get()))
        resultado13.set(float(cantidad13.get())*float(precio13.get()))
        resultado14.set(float(cantidad14.get())*float(precio14.get()))
        resultado15.set(float(cantidad15.get())*float(precio15.get()))

        resultadoT.set("Subtotal: "+ str(float(resultado1.get())+float(resultado2.get())+float(resultado3.get())+float(resultado4.get())+float(resultado5.get())+float(resultado6.get())+float(resultado7.get())+float(resultado8.get())+float(resultado9.get())+float(resultado10.get())+float(resultado11.get())+float(resultado12.get())+float(resultado13.get())+float(resultado14.get())+float(resultado15.get())))
        iva.set("Iva: " + str(0.12*(float(resultado1.get())+float(resultado2.get())+float(resultado3.get())+float(resultado4.get())+float(resultado5.get())+float(resultado6.get())+float(resultado7.get())+float(resultado8.get())+float(resultado9.get())+float(resultado10.get())+float(resultado11.get())+float(resultado12.get())+float(resultado13.get())+float(resultado14.get())+float(resultado15.get()))))


        resultadoTIVA.set("Total: " + str(1.12*(float(resultado1.get())+float(resultado2.get())+float(resultado3.get())+float(resultado4.get())+float(resultado5.get())+float(resultado6.get())+float(resultado7.get())+float(resultado8.get())+float(resultado9.get())+float(resultado10.get())+float(resultado11.get())+float(resultado12.get())+float(resultado13.get())+float(resultado14.get())+float(resultado15.get()))))
def limpiar():
    cliente.set("")
    ruc.set("")
    producto1.set("")
    producto2.set("")
    producto3.set("")
    producto4.set("")
    producto5.set("")
    producto6.set("")
    producto7.set("")
    producto8.set("")
    producto9.set("")
    producto10.set("")
    producto11.set("")
    producto12.set("")
    producto13.set("")
    producto14.set("")
    producto15.set("")


    cantidad1.set("")
    cantidad2.set("")
    cantidad3.set("")
    cantidad4.set("")
    cantidad5.set("")
    cantidad6.set("")
    cantidad7.set("")
    cantidad8.set("")
    cantidad9.set("")
    cantidad10.set("")
    cantidad11.set("")
    cantidad12.set("")
    cantidad13.set("")
    cantidad14.set("")
    cantidad15.set("")

    precio1.set("")
    precio2.set("")
    precio3.set("")
    precio4.set("")
    precio5.set("")
    precio6.set("")
    precio7.set("")
    precio8.set("")
    precio9.set("")
    precio10.set("")
    precio11.set("")
    precio12.set("")
    precio13.set("")
    precio14.set("")
    precio15.set("")

    resultado1.set("")
    resultado2.set("")
    resultado3.set("")
    resultado4.set("")
    resultado5.set("")
    resultado6.set("")
    resultado7.set("")
    resultado8.set("")
    resultado9.set("")
    resultado10.set("")
    resultado11.set("")
    resultado12.set("")
    resultado13.set("")
    resultado14.set("")
    resultado15.set("")
    resultadoT.set("")
    resultadoTIVA .set("")
    iva.set("")

tk.Label(text="FACTURA :) ", bg= "white").place(x=275,y=10)

tk.Label(text="Cliente: ", bg= "white").place(x=10,y=40)
tk.Label(text="RUC: ", bg= "white").place(x=10,y=70)



tk.Entry(textvariable = cliente,bd=1,width=45,justify="left").place(x=100,y=40)
tk.Entry(textvariable = ruc,bd=1,width=45,justify="left").place(x=100,y=70)

tk.Button(text="limpiar",width=10,height=1, bg= "Orange", command= limpiar).place(x=570,y=40)
tk.Button(text="calcular",width=10,height=1,bg= "Orange", command= calcular).place(x=570,y=70)

tk.Label(text="PRODUCTO ", bg= "white").place(x=100,y=100)
tk.Label(text="CANTIDAD ", bg= "white").place(x=220,y=100)
tk.Label(text="PRECIO U. ", bg= "white").place(x=320,y=100)
tk.Label(text="PRECIO T.", bg= "white").place(x=420,y=100)

tk.Label(text="Jefes: Alex Pérez, Pablo Reyes y Jim Simancas ", bg= "white").place(x=10,y=460)


tk.Entry(textvariable = producto1,bd=1,width=12,justify="left").place(x=90,y=130)


tk.Entry(textvariable = producto2,bd=1,width=12,justify="left").place(x=90,y=160)


tk.Entry(textvariable = producto3,bd=1,width=12,justify="left").place(x=90,y=190)


tk.Entry(textvariable = producto4,bd=1,width=12,justify="left").place(x=90,y=220)


tk.Entry(textvariable = producto5,bd=1,width=12,justify="left").place(x=90,y=250)


tk.Entry(textvariable = producto6,bd=1,width=12,justify="left").place(x=90,y=280)


tk.Entry(textvariable = producto7,bd=1,width=12,justify="left").place(x=90,y=310)
tk.Entry(textvariable = producto8,bd=1,width=12,justify="left").place(x=90,y=340)
tk.Entry(textvariable = producto9,bd=1,width=12,justify="left").place(x=90,y=370)
tk.Entry(textvariable = producto10,bd=1,width=12,justify="left").place(x=90,y=400)
tk.Entry(textvariable = producto11,bd=1,width=12,justify="left").place(x=90,y=430)
tk.Entry(textvariable = producto12,bd=1,width=12,justify="left").place(x=90,y=460)
tk.Entry(textvariable = producto13,bd=1,width=12,justify="left").place(x=90,y=490)
tk.Entry(textvariable = producto14,bd=1,width=12,justify="left").place(x=90,y=520)
tk.Entry(textvariable = producto15,bd=1,width=12,justify="left").place(x=90,y=550)


tk.Entry(textvariable = cantidad1,bd=1,width=5,justify="left").place(x=230,y=130)

tk.Entry(textvariable = cantidad2,bd=1,width=5,justify="left").place(x=230,y=160)

tk.Entry(textvariable = cantidad3,bd=1,width=5,justify="left").place(x=230,y=190)

tk.Entry(textvariable = cantidad4,bd=1,width=5,justify="left").place(x=230,y=220)

tk.Entry(textvariable = cantidad5,bd=1,width=5,justify="left").place(x=230,y=250)

tk.Entry(textvariable = cantidad6,bd=1,width=5,justify="left").place(x=230,y=280)

tk.Entry(textvariable = cantidad7,bd=1,width=5,justify="left").place(x=230,y=310)

tk.Entry(textvariable = cantidad8,bd=1,width=5,justify="left").place(x=230,y=340)

tk.Entry(textvariable = cantidad9,bd=1,width=5,justify="left").place(x=230,y=370)

tk.Entry(textvariable = cantidad10,bd=1,width=5,justify="left").place(x=230,y=400)

tk.Entry(textvariable = cantidad11,bd=1,width=5,justify="left").place(x=230,y=430)

tk.Entry(textvariable = cantidad12,bd=1,width=5,justify="left").place(x=230,y=460)

tk.Entry(textvariable = cantidad13,bd=1,width=5,justify="left").place(x=230,y=490)

tk.Entry(textvariable = cantidad14,bd=1,width=5,justify="left").place(x=230,y=520)

tk.Entry(textvariable = cantidad15,bd=1,width=5,justify="left").place(x=230,y=550)


tk.Entry(textvariable = precio1,bd=1,width=8,justify="left").place(x=315,y=130)

tk.Entry(textvariable = precio2,bd=1,width=8,justify="left").place(x=315,y=160)

tk.Entry(textvariable = precio3,bd=1,width=8,justify="left").place(x=315,y=190)

tk.Entry(textvariable = precio4,bd=1,width=8,justify="left").place(x=315,y=220)

tk.Entry(textvariable = precio5,bd=1,width=8,justify="left").place(x=315,y=250)

tk.Entry(textvariable = precio6,bd=1,width=8,justify="left").place(x=315,y=280)

tk.Entry(textvariable = precio7,bd=1,width=8,justify="left").place(x=315,y=310)

tk.Entry(textvariable = precio8,bd=1,width=8,justify="left").place(x=315,y=340)

tk.Entry(textvariable = precio9,bd=1,width=8,justify="left").place(x=315,y=370)

tk.Entry(textvariable = precio10,bd=1,width=8,justify="left").place(x=315,y=400)

tk.Entry(textvariable = precio11,bd=1,width=8,justify="left").place(x=315,y=430)

tk.Entry(textvariable = precio12,bd=1,width=8,justify="left").place(x=315,y=460)

tk.Entry(textvariable = precio13,bd=1,width=8,justify="left").place(x=315,y=490)

tk.Entry(textvariable = precio14,bd=1,width=8,justify="left").place(x=315,y=520)

tk.Entry(textvariable = precio15,bd=1,width=8,justify="left").place(x=315,y=550)


tk.Label(textvariable = resultado1, bg="white", bd=1,width=8,justify="left").place(x=420,y=130)

tk.Label(textvariable = resultado2, bg="white", bd=1,width=8,justify="left").place(x=420,y=160)

tk.Label(textvariable = resultado3, bg="white", bd=1,width=8,justify="left").place(x=420,y=190)

tk.Label(textvariable = resultado4, bg="white", bd=1,width=8,justify="left").place(x=420,y=220)

tk.Label(textvariable = resultado5, bg="white", bd=1,width=8,justify="left").place(x=420,y=250)

tk.Label(textvariable = resultado6, bg="white", bd=1,width=8,justify="left").place(x=420,y=280)

tk.Label(textvariable = resultado7, bg="white", bd=1,width=8,justify="left").place(x=420,y=310)

tk.Label(textvariable = resultado8, bg="white", bd=1,width=8,justify="left").place(x=420,y=340)

tk.Label(textvariable = resultado9, bg="white", bd=1,width=8,justify="left").place(x=420,y=370)

tk.Label(textvariable = resultado10, bg="white", bd=1,width=8,justify="left").place(x=420,y=400)

tk.Label(textvariable = resultado11, bg="white", bd=1,width=8,justify="left").place(x=420,y=430)

tk.Label(textvariable = resultado12, bg="white", bd=1,width=8,justify="left").place(x=420,y=460)

tk.Label(textvariable = resultado13, bg="white", bd=1,width=8,justify="left").place(x=420,y=490)

tk.Label(textvariable = resultado14, bg="white", bd=1,width=8,justify="left").place(x=420,y=520)

tk.Label(textvariable = resultado15, bg="white", bd=1,width=8,justify="left").place(x=420,y=550)


tk.Label(textvariable = resultadoT,justify="left").place(x=370,y=350)
tk.Label(textvariable = iva,justify="left").place(x=370,y=380)
tk.Label(textvariable = resultadoTIVA ,justify="left").place(x=480,y=10)

ventana.mainloop()
