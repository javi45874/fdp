#hacer un listado de compras: frutas,verduras,cereales, carnes. cada grupo debe tener al menos 2 elementos pertenecientes. 
#debe ser un diccionario con varios diccionarios adentro
#se debe listar por grupo despues

lista_productos={
    "frutas":{
        "uva":1800, "manzana":2100
    },
    "verduras":{
        "papas":5000, "zanahorias":3200
    },
    "cereales":{
        "chocapic":5600,"zucaritas":4800
    },
    "carnes":{
        "puerco":8990, "vacuno":10000
    }
    }

#opcion1 para listar
# for diccionario in lista_productos:
#     print(diccionario, '',lista_productos[diccionario])

# for key in lista_productos:
#     print(key,";")
#     for elemento in lista_productos[key]:
#         print(elemento,":",lista_productos[key][elemento])

#print(lista_productos["cereales"]["zucaritas"])#asi me va a mostrar especificamente el valor de las zucaritas

print("zucaritas",":",lista_productos["cereales"]["zucaritas"])


