# el signo igual es para asignar, == es para comparar
#en la comparativa el num para comparar estaba entre parentesis
taco=1
pizza=2
humitas=3
cazuela=4

print("elija una opción de comida")
opc=int(input())

if opc==1:
    print("a usted le gustan los tacos")

elif opc==2:
  print("a usted le gustan las pizzas")

elif opc==3:
    print("a usted le gustan las humitas")

elif opc==4:
    print("a usted le gustan las cazuelas")

else:
    print("opcion no valida")