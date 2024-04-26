# def suma(num1, num2):
#     resul=num1+num2
#     return resul
# def resta(num1, num2):
#     resul=num1-num2
#     return resul

def multi (num1,num2,num3):
    resultado=(num1*num2)-num3
    return resultado

def division (num1,num2,num3):
    resultado=(num1/num2)
    return resultado

print("Ingrese tres numeros")
num1=int(input())
num2=int(input())
num3=int(input())
print(multi(num1,num2,num3))
