def verifpassw():
 
 print("Ingrese su password ")
 passw=input()
 while passw !="1234":
    print("Su password es incorrecta")
    passw=input()
 
 print("Bienvenido Usuario Admin")

# verifpassw()

def multiplicar(num1,num2,num3):
   multi=(num1*num2)-num3
   return multi
 
#multiplicar()

def division (num1,num2,num3):
    resultado=(num1/num2)
    return resultado
#division()

def formula(num1,num2,num3):
   formu=(num1*num2)/(num2*num3)
   return formu
# formula()
  
   

print("escoge una opción")
print("opc1:verificador formula")
print("opc2:multiplicación")
print("opc3:división")
print("opc4:formula")
print("opc5:regresa al menu principal")


opc=int(input())
while opc !=5:
   
    match opc:
        case 1: 
            verifpassw()
        case 2:
            print("ingrese tres numeros")
            num1=int(input())
            num2=int(input())
            num3=int(input())
            print(multiplicar(num1,num2,num3))
        case 3:
            print("ingrese tres numeros")
            num1=int(input())
            num2=int(input())
            num3=int(input())
            print(division(num1,num2))
        case 4:
            print("ingrese tres numeros")
            num1=int(input())
            num2=int(input())
            num3=int(input())
            print(formula(num1,num2,num3)) 
    

    