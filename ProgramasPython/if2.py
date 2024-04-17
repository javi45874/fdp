#evaluar que numero es mayor entre los3
print("elige el primer n° a evaluar")
num1=int(input())
print("elige el segundo n° a evaluar")
num2=int(input())
print("elige el segundo n° a evaluar")
num3=int(input())

if num1>num2 and num1>num3:
    print("el numero mayor es", num1)
if num2>num3:
    print("el numero mayor es ",num2)
else:
    print("el numero mayor es ", num3)