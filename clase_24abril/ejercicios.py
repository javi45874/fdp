# #ejercicio1
# print("ingrese un numero")
# numero=int(input())

# for i in range(1,numero+1,2):
#     print(i,end=",")
# # el range tiene mas opciones (enque numero empieza, cual es el limite max, cuanto va a sumar)
# #si pongo end al final, me concatena todos los resultados que arroja el for, en el ejemplo agrego una coma

#ejercicio2:Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# print("ingrese un numero entero positivo")
# numero=int(input())

# while numero!= 0:
#     numero=numero-1
#     print(numero, end=",")

#opcion2
# print("ingrese un numero entero positivo")
# numero=int(input())
# for i in range(numero,-1,-1):
#     print(i, end=",")

#ejercicio3:Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
#el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# print("ingrese monto incial")
# monto_inicial=int(input())
# print("ingrese el interes anual")
# interes=float(input())
# print("ingrese años de duracion de la inversión")
# años=int(input())

# for i in range(años):
#     monto_inicial=monto_inicial*(1+(interes/100))
#     print("en el año",i,"ganas",monto_inicial,"pesos")#recordar: yo le dije al sistema que monto_inicial partia con el valor dado en la terminar, al usarlo para que agregue la cantidad
#     #final, hago que el valor vaya cambiando en cada iteración.

# print("ingrese monto incial")
# monto_inicial=int(input())

# interes=22.5
# print("ingrese años de duracion de la inversión")
# años=int(input())
# for i in range(años):
#     monto_inicial=monto_inicial*(1+(interes/100))
#     print("en el año",i+1,"ganas",round(monto_inicial,3),"pesos")#recordar: yo le dije al sistema que monto_inicial partia con el valor dado en la terminar, al usarlo para que agregue la cantidad
#     #final, hago que el valor vaya cambiando en cada iteración.

#ejercicio3:triangulito
print("ingrese un numero")
numero=int(input())

for i in range(numero):
    print("*"*(i+1))