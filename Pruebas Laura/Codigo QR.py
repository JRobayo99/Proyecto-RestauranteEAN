f=[]
b=[]
e=[]
import qrcode
img = qrcode.make()
print("__Menú central__")
print("1) Menu del día y personalizar pedido")
print("2) Reservación de dia para restaurante")
print("3) Entrada y Salida de trabajadores")
mnu1=int(input("Seleccione la opción de: "))
for i in range(1,4):
  if(mnu1==1):
    f = open("Menu del Desayuno.png", "wb")
    img.save(f)
    f.close()
  if(mnu1==2):
    b = open("Reservación.png", "wb")
    img.save(b)
    f.close()
  if(mnu1==3):
    e = open("Empleados.png", "wb")
    img.save(e)
    f.close()
f=[]
b=[]
e=[]
#Holi UwU