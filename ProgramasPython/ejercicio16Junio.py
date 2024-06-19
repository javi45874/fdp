#bitacora auto: resgistro como texto de las acciones encender auto, colocar alarma, auto encendido, auto estacionado, auto con nivel de aceite bajo, etc.
#usar while, for, listas, try except, validaciones, archivos csv y funciones
#menu de opciones: primera opcion agregar acciones a la lista, segunda opcion es para ver las bitacoras hechas en el auto, tercera opcion guarda la bitacora como archivo csv, 
# cuarta opcion para salir
# reglas del negocio:
# 1. las acciones se guardan con la fecha y hora actual"dd-mm-yyyy hh:mm:ss"-libreria "from datetime import datetime"
# 2. el usuario debe guardar el archivo con el nombre y extension
# 3. debe tener un menu de opciones
# si el archivo csv ya existe, se debe sobreescribir. 

bitacora=["a","b","c"]
from datetime import datetime
import csv

def agregar_evento(evento):
    
    now=datetime.now().strftime("%d-%m-%Y %h:%m:%S")
    fecha_evento=f"{now}-{evento}"
    bitacora.append(fecha_evento)
    print(f"evento '{evento}' registrado")

def ver_bitacoras():
    if not bitacora:
        print("bitacora vacia")
    else:
            for elemento in bitacora:
                print(elemento)
def guardar_archivo(nombre_archivo):
        with open(nombre_archivo, mode='w',newline="") as archivo_csv:
        writer=csv.writer(archivo_csv)
        writer.writerow(['Bitácora del Auto'])
            for i in bitacora:
             writer.writerow([evento])

print("ingrese su nombre")
nombre=input()
while True:
        
    print("""Elige una opción"
    "1. Agregar evento o acción"
    "2. ver bitacora guardada"
    "3. Guardar bitacora como csv"
    "4. finalizar programa
          """)
    opcion=int(input())

    match opcion:
        case 1: 
            print("que evento o accion quieres agregar?")
            evento=input()
            agregar_evento(evento)
        case 2:
            ver_bitacoras()