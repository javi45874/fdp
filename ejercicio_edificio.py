#crear programa que registra cuartos de hotel, tiene 10 pisos, cada piso tiene 6 habitaciones, registrar pasajeros en las habitaciones, mostrar reporte de habitaciones ocupadas
#y guardarlo en un archivo.
#none verifica si esta vacio, tiene que recorrer todo lo que hay

edificios=[[[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]]
]


while True:
    print("""Elige una opción:
     1.Reservar habitación
     2.Actualizar info habitación
     3.Ver todas las habitaciones
     4.Guardar en un archivo
     5.Finalizar programa
      """)
    opcion=int(input())

    match opcion:
     case 1: 
            print("Ingrese piso") 
            piso=int(input())
            while piso<1 or piso>10:
                   print("opcion invalida")
                   print("en que habitación se va a alojar?")
                   piso=int(input())
            print("Ingrese habitacion") 
            habitacion=int(input())
            if edificios[piso-1][habitacion-1]:
                print("Habitacion ocupada")
            else:
                print("Ingrese nombre pasajero") 
                pasajero=input() 
                edificios[piso-1][habitacion-1]=[pasajero]
     case 2:
            print("que piso quiere actualizar?")
            pisoo=int(input)
            print("que habitacion quiere actualizar?")
            hab=int(input)
            edificios[pisoo-1][hab-1]=[]
     case 3:
              for pis in edificios:
                   print(pis)
     case 4:
              with open("hotel.txt","w") as archivo:
                     
     case 5:
                break
     case _: 
                print("opcion ingresada no es valida")





 




    


    
    