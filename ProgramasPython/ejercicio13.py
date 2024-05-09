# print("ingrese su edad")
# edad=int(input())

# print ("ingrese cantidad de productos comprados")
# Qprod=int(input())

# cumple=False

# if edad>=18 and Qprod>1:
#     cumple=True
#     print ("edad",edad)
#     print ("cantidad productos",Qprod)
#     print (cumple)
# else: 
#     print ("edad",edad)
#     print ("cantidad productos",Qprod)
#     print (cumple)

# #año biciesto
# print("ingrese un año")
# año=int(input())    

# if año%4==0 and año%100 !=0:
#     if año%400==0:
#         print("año biciesto")
#     if año%100==0 and año%4!=0:
#         print("año normal")

print("ingresa tu nombre")
nombre=input()
print("ingresa una letra")
let=input()
contador=0

for letras in nombre:
    if letras==let:
        contador=contador+1
print(contador)