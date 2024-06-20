#crear programa que registra cuartos de hotel, tiene 10 pisos, cada piso tiene 6 habitaciones, registrar pasajeros en las habitaciones, mostrar reporte de habitaciones ocupadas
#y guardarlo en un archivo.
#none verifica si esta vacio, tiene que recorrer todo lo que hay

edificios={{{},{},{},{},{},{}},
           {{},{},{},{},{},{}},
           {{},{},{},{},{},{}},
           {{},{},{},{},{},{}},
           {{},{},{},{},{},{}},
           {{},{},{},{},{},{}},
           {{},{},{},{},{},{}},
           {{},{},{},{},{},{}},
           {{},{},{},{},{},{}},
           {{},{},{},{},{},{}},
}
    
print("Ingrese nombre pasajero") 
pasajero=input()   
print("Ingrese piso") 
piso=int(input())-1
print("Ingrese habitacion") 
habitacion=int(input())-1
[piso],[habitacion]=[pasajero]

for pisos in edificios:
    print("piso",pisos)
    for habi in pisos:
        print("habitacion",habi)


    
    