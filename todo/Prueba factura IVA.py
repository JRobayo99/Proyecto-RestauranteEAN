print("Ingrese el nombre del primer producto")
p1=input()
print("cantidad comprada de",p1)
p1_cant=int(input())
print("valor de la unidad de",p1)
p1_vu = int(input())

print("ingrese el nombre del segundo procuto")
p2=input()
print("cantidad comprada de",p2)
p2_cant = int(input())
print("valor de la unidad de",p2)
p2_vu = int(input())

print("ingrese el nombre del tercer procuto")
p3=input()
print("cantidad comprada de",p3)
p3_cant = int(input())
print("valor de la unidad de",p3)
p3_vu = int(input())

p1_st = p1_cant * p1_vu
p2_st = p2_cant * p2_vu
p3_st = p3_cant * p3_vu

SubTot = p1_st + p2_st + p3_st
IVA = SubTot * 0.19
Total = SubTot + IVA

print("El total a pagar por",p1," es: ",p1_st)
print("El total a pagar por",p2," es: ",p2_st)
print("El total a pagar por",p3," es: ",p3_st)
print("El subtotal de la factura es:",SubTot)
print("El IVA fue:",IVA)
print("El total a pagar con IVA es:",Total)
