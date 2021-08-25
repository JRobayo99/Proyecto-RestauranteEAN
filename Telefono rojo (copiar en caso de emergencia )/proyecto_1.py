print("__Menú central__")
print("1) Menu del día y personalizar pedido")
print("2) Reservación de dia para restaurante")
print("3) Entrada y Salida de trabjadores")
mnu1=int(input("Seleccione la opción de: "))
if(mnu1==1):
 print ("__Menú del día__")
 print("1) Desayuno")
 print("2) Almuerzo")
 print("3) Cena")

 tipom=int(input("Seleccione el tipo de menú:  "))
 if (tipom==1):
   print("Menu del Desayuno")
   print("1) Huevos revueltos con chocolate")
   print("2) Tamal con chocolate")
   print("3) Arepa con queso y chocolate")
   print("4) Changua con café")
   print("5) Caldo de costilla con cafe con leche")
   a=int(input("¿Qué desea ordenar?: "))
   if(a==1):
     print("Su orden de Huevos revueltos con chocolate estará lista en unos minutos")
   elif(a==2):
     print("Su orden de Tamal con chocolate estará lista en unos minutos")
   elif(a==3):
     print("Su orden de Arepa con queso y chocolate estará lista en unos minutos")
   elif(a==4):
     print("Su orden de Changua con café estará lista en unos minutos")
   elif(a==5):
     print("Su orden de Caldo de costilla con cafe con leche estará lista en unos minutos")
 elif(tipom==2):
     print("Menú del Almuerzo")
     print("Sopas")
     print("1) Sopa de mondongo")
     print("2) Sopa de arroz")
     print("3) Sopa de pasta")
     b=int(input("¿Qué sopa desea ordenar?: "))
     print("Principio")
     print("1) Arroz con frijol, carne, patacones y ensalada")
     print("2) Mojarra frita con papa salada y ensalada")
     print("3) Arroz con pasta, papa salada y chuleta")
     c=int(input("¿Qué principio desea ordenar?: "))
     print("Sobremesa")
     print("1) Jugo de lulo")
     print("2) Jugo de maracuyá")
     print("3) Limonada")
     d=int(input("¿Qué sobremesa desea ordenar?: "))
     if(b==1 and c==1 and d==1):
        print("Su orden de Sopa de mondongo + Arroz con frijol, carne, patacones y ensalada + Jugo de lulo estará lista en unos minutos")
     elif(b==1 and c==2 and d==1):
         print("Su orden de Sopa de mondongo + Mojarra frita con papa salada y ensalada + Jugo de lulo estará lista en unos minutos")
     elif(b==1 and c==3 and d==1):
         print("Su orden de Sopa de mondongo + Arroz con pasta, papa salada y chuleta + Jugo de lulo estará lista en unos minutos")
     elif(b==1 and c==1 and d==2):
         print("Su orden de Sopa de mondongo + Arroz con frijol, carne, patacones y ensalada + Jugo de maracuyá estará lista en unos minutos")
     elif(b==1 and c==2 and d==2):
         print("Su orden de Sopa de mondongo + Mojarra frita con papa salada y ensalada + Jugo de maracuyá estará lista en unos minutos")
     elif(b==1 and c==3 and d==2):
          print("Su orden de Sopa de mondongo + Arroz con pasta, papa salada y chuleta + Jugo de maracuyá estará lista en unos minutos")
     elif(b==1 and c==1 and d==3):
         print("Su orden de Sopa de mondongo + Arroz con frijol, carne, patacones y ensalada + Limonada estará lista en unos minutos")
     elif(b==1 and c==2 and d==3):
         print("Su orden de Sopa de mondongo + Mojarra frita con papa salada y ensalada + Limonada estará lista en unos minutos")
     elif(b==1 and c==3 and d==3):
         print("Su orden de Sopa de mondongo + Arroz con pasta, papa salada y chuleta + Limonada estará lista en unos minutos")
     elif(b==2 and c==1 and d==1):
         print("Su orden de Sopa de arroz + Arroz con frijol, carne, patacones y ensalada + Jugo de lulo estará lista en unos minutos")
     elif(b==2 and c==2 and d==1):
         print("Su orden de Sopa de arroz + Mojarra frita con papa salada y ensalada + Jugo de lulo estará lista en unos minutos")
     elif(b==2 and c==3 and d==1):
        print("Su orden de Sopa de arroz + Arroz con pasta, papa salada y chuleta + Jugo de lulo estará lista en unos minutos")
     elif(b==2 and c==1 and d==2):
         print("Su orden de Sopa de arroz + Arroz con frijol, carne, patacones y ensalada + Jugo de maracuyá estará lista en unos minutos")
     elif(b==2 and c==2 and d==2):
         print("Su orden de Sopa de arroz + Mojarra frita con papa salada y ensalada + Jugo de maracuyá estará lista en unos minutos")
     elif(b==2 and c==3 and d==2):
         print("Su orden de Sopa de arroz + Arroz con pasta, papa salada y chuleta + Jugo de maracuyá estará lista en unos minutos")
     elif(b==2 and c==1 and d==3):
         print("Su orden de Sopa de arroz + Arroz con frijol, carne, patacones y ensalada + Limonada estará lista en unos minutos")
     elif(b==2 and c==2 and d==3):
         print("Su orden de Sopa de arroz + Mojarra frita con papa salada y ensalada + Limonada estará lista en unos minutos")
     elif(b==2 and c==3 and d==3):
         print("Su orden de Sopa de arroz + Arroz con pasta, papa salada y chuleta + Limonada estará lista en unos minutos")
     elif(b==3 and c==1 and d==1):
         print("Su orden de Sopa de pasta + Arroz con frijol, carne, patacones y ensalada + Jugo de lulo estará lista en unos minutos")
     elif(b==3 and c==2 and d==1):
         print("Su orden de Sopa de pasta + Mojarra frita con papa salada y ensalada + Jugo de lulo estará lista en unos minutos")
     elif(b==3 and c==3 and d==1):
         print("Su orden de Sopa de pasta + Arroz con pasta, papa salada y chuleta + Jugo de lulo estará lista en unos minutos")
     elif(b==3 and c==1 and d==2):
         print("Su orden de Sopa de pasta + Arroz con frijol, carne, patacones y ensalada + Jugo de maracuyá estará lista en unos minutos")
     elif(b==3 and c==2 and d==2):
         print("Su orden de Sopa de pasta + Mojarra frita con papa salada y ensalada + Jugo de maracuyá estará lista en unos minutos")
     elif(b==3 and c==3 and d==2):
        print("Su orden de Sopa de arroz + Arroz con pasta, papa salada y chuleta + Jugo de maracuyá estará lista en unos minutos")
     elif(b==3 and c==1 and d==3):
         print("Su orden de Sopa de pasta + Arroz con frijol, carne, patacones y ensalada + Limonada estará lista en unos minutos")
     elif(b==3 and c==2 and d==3):
         print("Su orden de Sopa de pasta + Mojarra frita con papa salada y ensalada + Limonada estará lista en unos minutos")
     elif(b==2 and c==3 and d==3):
         print("Su orden de Sopa de pasta + Arroz con pasta, papa salada y chuleta + Limonada estará lista en unos minutos")
 elif (tipom==3):
     print("Menú de Cena")
     print("Sopas")
     print("1) Crema de champiñones")
     print("2) Sopa de verduras")
     print("3) Agiaco")
     b=int(input("¿Qué sopa desea ordenar?: "))
     print("Principio")
     print("1) Arroz, papa frita, ensalada y sobrebarriga")
     print("2) Arroz, plátano frito, ensalada y pechuga a la plancha")
     print("3) Arroz con lentejas, papas fritas y churrasco")
     c=int(input("¿Qué principio desea ordenar?: "))
     print("Sobremesa")
     print("1) Jugo de lulo")
     print("2) Jugo de maracuyá")
     print("3) Limonada")
     d=int(input("¿Qué sobremesa desea ordenar?: "))
     if(b==1 and c==1 and d==1):
         print("Su orden de Crema de champiñones + Arroz, papa frita, ensalada y sobrebarriga + Jugo de lulo estará lista en unos minutos")
     elif(b==1 and c==2 and d==1):
          print("Su orden de Crema de champiñones + Arroz, plátano frito, ensalada y pechuga a la plancha + Jugo de lulo estará lista en unos minutos")
     elif(b==1 and c==3 and d==1):
         print("Su orden de Crema de champiñones + Arroz con lentejas, papas fritas y churrasco + Jugo de lulo estará lista en unos minutos")
     elif(b==1 and c==1 and d==2):
         print("Su orden de Crema de champiñones + Arroz,papa frita, ensalada y sobrebarriga + Jugo de maracuyá estará lista en unos minutos")
     elif(b==1 and c==2 and d==2):
         print("Su orden de Crema de champiñones + Arroz,plátano frito, ensalada y pechuga a la plancha + Jugo de maracuyá estará lista en unos minutos")
     elif(b==1 and c==3 and d==2):
         print("Su orden de Crema de champiñones +  Arroz con lentejas, papas fritas y churrasco + Jugo de maracuyá estará lista en unos minutos")
     elif(b==1 and c==1 and d==3):
         print("Su orden de Crema de champiñones + Arroz,papa frita, ensalada y sobrebarriga + Limonada estará lista en unos minutos")
     elif(b==1 and c==2 and d==3):
         print("Su orden de Crema de champiñones + Arroz,plátano frito, ensalada y pechuga a la plancha + Limonada estará lista en unos minutos")
     elif(b==1 and c==3 and d==3):
         print("Su orden de Crema de champiñones +  Arroz con lentejas, papas fritas y churrasco + Limonada estará lista en unos minutos")
     elif(b==2 and c==1 and d==1):
         print("Su orden de Sopa de verduras + Arroz,papa frita, ensalada y sobrebarriga + Jugo de lulo estará lista en unos minutos")
     elif(b==2 and c==2 and d==1):
         print("Su orden de Sopa de verduras + Arroz,plátano frito, ensalada y pechuga a la plancha + Jugo de lulo estará lista en unos minutos")
     elif(b==2 and c==3 and d==1):
         print("Su orden de Sopa de verduras + Arroz con lentejas, papas fritas y churrasco + Jugo de lulo estará lista en unos minutos")
     elif(b==2 and c==1 and d==2):
         print("Su orden de Sopa de verduras + Arroz,papa frita, ensalada y sobrebarriga + Jugo de maracuyá estará lista en unos minutos")
     elif(b==2 and c==2 and d==2):
         print("Su orden de Sopa de verduras + Arroz,plátano frito, ensalada y pechuga a la plancha + Jugo de maracuyá estará lista en unos minutos")
     elif(b==2 and c==3 and d==2):
         print("Su orden de Sopa de verduras + Arroz con lentejas, papas fritas y churrasco + Jugo de maracuyá estará lista en unos minutos")
     elif(b==2 and c==1 and d==3):
         print("Su orden de Sopa de verduras + Arroz,papa frita, ensalada y sobrebarriga + Limonada estará lista en unos minutos")
     elif(b==2 and c==2 and d==3):
         print("Su orden de Sopa de verduras + Arroz,plátano frito, ensalada y pechuga a la plancha + Limonada estará lista en unos minutos")
     elif(b==2 and c==3 and d==3):
         print("Su orden de Sopa de verduras + Arroz con lentejas, papas fritas y churrasco + Limonada estará lista en unos minutos")
     elif(b==3 and c==1 and d==1):
         print("Su orden de Agiaco + Arroz,papa frita, ensalada y sobrebarriga + Jugo de lulo estará lista en unos minutos")
     elif(b==3 and c==2 and d==1):
         print("Su orden de Agiaco + Arroz,plátano frito, ensalada y pechuga a la plancha + Jugo de lulo estará lista en unos minutos")
     elif(b==3 and c==3 and d==1):
         print("Su orden de Agiaco + Arroz con lentejas, papas fritas y churrasco + Jugo de lulo estará lista en unos minutos")
     elif(b==3 and c==1 and d==2):
         print("Su orden de de Agiaco + Arroz,papa frita, ensalada y sobrebarriga + Jugo de maracuyá estará lista en unos minutos")
     elif(b==3 and c==2 and d==2):
         print("Su orden de Agiaco + Arroz,plátano frito, ensalada y pechuga a la plancha + Jugo de maracuyá estará lista en unos minutos")
     elif(b==3 and c==3 and d==2):
         print("Su orden de Agiaco + Arroz con lentejas, papas fritas y churrasco + Jugo de maracuyá estará lista en unos minutos")
     elif(b==3 and c==1 and d==3):
         print("Su orden de Agiaco + Arroz,papa frita, ensalada y sobrebarriga + Limonada estará lista en unos minutos")
     elif(b==3 and c==2 and d==3):
         print("Su orden de Agiaco + Arroz,plátano frito, ensalada y pechuga a la plancha + Limonada estará lista en unos minutos")
     elif(b==3 and c==3 and d==3):
         print("Su orden de Agiaco + Arroz con lentejas, papas fritas y churrasco + Limonada estará lista en unos minutos")
if(mnu1==2):
   print("--Dia reservación--")
   print ("1) lunes")
   print ("2) martes")
   print ("3) miercoles")
   print ("4) jueves")
   print ("5) viernes")
   print ("6) Sabado")
   print ("7) Domingo")
   dia_dr= int(input("Selelcciona el dia para tu reservacion: ")) 
   if dia_dr==1 or dia_dr==3 or dia_dr==5:
      print ("Este dia solo tenemos capacidad para 80 personas")
      print ("Desea reservar este dia: ")
      print ("1) Si")
      print ("2) No")
      esd_1= int(input("Selecciona 1 para reservar ese dia y 2 para no: "))
      if (esd_1==1):
          print("Reservación hecha")
      elif (esd_1==2):
          print("Vuelve a seleccionar el dia")
   elif dia_dr==2 or dia_dr==4 or dia_dr==6 or dia_dr==7:
       print ("Este dia tenemos cacidad para 100 personas")
       print ("Desea reservar este dia: ")
       print ("1) Si")
       print ("2) No")
       esd_1= int(input("Selecciona 1 para reservar ese dia y 2 para no: "))
       if (esd_1==1):
         print("Reservación hecha")
       elif (esd_1==2):
         print("Vuelve a seleccionar el dia")
if(mnu1==3):
    n=input("Ingrese su nombre: ")
    f=input("Ingrese su funcion: ")
    c=int(input("Ingrese 1 para entrada o 2 para salida: "))
    if(c==1):
      print("Entrada")
    elif (c==2):
     print("Salida")
    import datetime
    ahora=datetime.datetime.now()
    print(ahora)
