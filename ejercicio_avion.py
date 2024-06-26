#crear una reserva de un avion, 6 asientos, 16 filas de asientos
#se debe reservar con el nombre, rut
#hay tres clases dentro del avion : economica, turista y ejecutivo
#cuidado con el manejo de errores, como tratar de poner a un pasajero en asiento/fila existente


economica=[[[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
]
turista=[[[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
]

ejecutivo=[[[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
           [[],[],[],[],[],[]],
]




while True:
    print("""en que clase desea viajar?
          1. Economica
          2. Turista
          3. Ejecutiva
          4. Finalizar programa
          """)
    opcion=int(input())
    match opcion:
        case 1:
            print("Que fila quiere?")
            fila=int(input())-1
            while fila<0 or fila>16:
                print("fila invalida, por favor ingresa una fila valida del 1 al 16")
                print("Que fila quiere?")
                fila=int(input())
            print("Que asiento quiere?")
            asiento=int(input())-1
            while fila<0 or fila>6:
              print("Asiento invalido, por favor ingresa un asiento valido del 1 al 16")
              print("Que asiento quiere?")
              asiento=int(input())
            if not economica[fila][asiento]:
               print("ingrese su nombre")
               pasajero=str(input())
               economica[fila][asiento]=pasajero
               print(f'ha reservado con exito el asiento {asiento}, en la fila {fila}')
            else:
                print(f'el asiento {asiento} en la fila {fila} ya esta ocupado, por favor selecciona otro')

        case 2:
            print("Que fila quiere?")
            fila=int(input())
            print("Que asiento quiere?")
            asiento=int(input())
            print("ingrese su nombre")
            pasajero=str(input())
            print("ingrese su rut")
            rut=int(input())
            turista[fila][asiento]=pasajero
            print(f'ha reservado con exito el asiento {asiento}, en la fila {fila}')

        case 3:
            print("Que fila quiere?")
            fila=int(input())
            print("Que asiento quiere?")
            asiento=int(input())
            print("ingrese su nombre")
            pasajero=str(input())
            print("ingrese su rut")
            rut=int(input())
            ejecutivo[fila][asiento]=pasajero
            print(f'ha reservado con exito el asiento {asiento}, en la fila {fila}')