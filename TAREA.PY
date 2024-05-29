# Realizar un menú el cual se vea asi

# Bienvenido al Parking VIP
# ¿que desea hacer?
# 1.- Ingresar un vehículo
# 2.- Listar vehículos
# 3.- Borrar un vehículo
# 4.- Conteo de vehículos
# 5.- Salir

# ​En la opción 1 debe aparecer --HECHO
# Selecciones el piso al cual quiere ingresar el vehículo

# La opción 2 debe aparecer
# 1.- Listar todos--hecho
# 2.- Listar un piso específico--hecho
# 3.- Volver--???

# La opción 3 debe aparecer
# Ingrese el vehículo a borrar

# La opción 4 debe salir
# 1.- Mostar cantidad de vehículos en total
# 2.- Mostar cantidad de vehículos por piso
# 3.- Mostar cantidad de vehículos de un piso
# 4.- Volver

# Requisitos
# USAR LISTAS
# La torre tiene 4 pisos
# El menú claremente debe ser recursivo
# No se puede ingresar una patente con mas de 6 caracteres
# El ingreso de patentes debe ser con el formato AABB99 0 AA8899

contador=0
check=True
STAY=True
matriz_autos=[
    ["AAAA01","AABB01","AACC01"],
    ["BBBB02","BBCC02"],
    ["CCCC03","CCDD03"],
    ["DDDD04","DDEE04"]
]



while check==True:
    print("¿Qué desea hacer")
    print("1.- Ingresar un vehículo")
    print("2.- Listar vehículos")
    print("3.- Borrar un vehículo")
    print("4.- Conteo de vehículos")
    print("5.- Salir")
    opcion=int(input())

    match opcion:
        case 1:
            print("Ingrese la patente que desea agregar")
            agrePatente=input()
            if agrePatente!=6:
                print("patente no valida, ingresa otra!")
                      print("Ingrese la patente que desea agregar")
            agrePatente=input()      
          
        case 2: 
           while STAY:
                print("Seleccione su opción:")
                print("1.- Listar todos")
                print("2.- Listar un piso específico")
                print("3.- Volver")
                opcion2=int(input())
                match opcion2:
                        case 1:
                            for elemento in matriz_autos:
                                for autos in elemento:
                                    print(autos)
                        case 2:
                            print("¿Qué piso desea ver")
                            Piso=int(input())
                            print(matriz_autos[Piso])
                        case 3:
                            STAY=False
                            print("opción finalizada, volveremos al menu principal!")
        case 3:
            print("¿En qué piso desea Borrar el vehiculo?")
            borrarAut=int(input())
            print("¿Qué patente desea eliminar?")
            boorarPatente=input()
            matriz_autos[borrarAut].remove(boorarPatente)
            print(matriz_autos[borrarAut])
        case 4:
            while STAY:
                print("Eliga que opcion de conteo de vehiculos desea")
                print("1.- Mostar cantidad de vehículos en total")
                print("2.- Mostar cantidad de vehículos por piso")
                print("3.- Mostar cantidad de vehículos de un piso")
                print("4.- Volver")
                opcion4=int(input())
                match opcion4:#terminar de agregar que me devuelva al menu principal
                    case 1:
                        for pisos in matriz_autos:
                            for veh in pisos:
                                contador=contador+1
                        print("el total de vehiculos es",contador)
                    case 2:
                        for pisos in matriz_autos:
                            print("la cantidad de autos en cada piso es",len(pisos))#arreglar esto para que me mueste en que piso es cada cosa
                    case 3:
                        print("Qué piso desea contar?")
                        pisoContar=int(input())
                        print("La cantidad de autos en el piso",pisoContar, "es",len(matriz_autos[pisoContar]))
                    case 4:
                        print("opcion finalizada, volveremos al menu principal!")
                        STAY=False
        case 5:
            opcion=5
            print("programa terminado!")    