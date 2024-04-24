#tarea:hacer un match para que el usuario tenga 3 opc. correr una de las funciones que ya creamos
errorr=input("introduzca un codigo de error")
match errorr:
    case "200":
        print("todo ok")
    case "301":
        print("algo1")
    case "302":
        print("algo2")
    case "404":
        print("page not found")
print("error no encontrado")