# Ingresar nombre de alumno
# Ingresar carrera 1 2 3
# la carrera 1 dura 8 semestres
# la carrera 2 dura 10 semestres
# la carrera 3 dura 6 semestres
# Basado en la información anterior calcular
# Calcular el total por año
# Calcular el valor total por carrera
# Consideraciones
# El valor mensual es de 300.000
# Si la carrera dura más de 6 semestres, tiene descuento de 15%(anual asumo)
# Cada semestre consta de 5 meses

# print("ingrese su nombre")
# nombre_alumno=input()

def valor_anual(meses):
    costomensual=300000
    vanual=meses*300000
    return vanual
    



        

    
    
    
        
# match carrera:
#     case 1: 
#         if carrera1_sem>6:
#             valor_carrera_anual=(meses_semestre*2)*valor_mensual#pasar esto a formula
#             descuento=valor_carrera_anual-(valor_carrera_anual*descuento)#pasar esto a formula
#             valor_total_carrera=descuento*(carrera1_sem/2)
#             print("alumno",nombre_alumno,"su cuota anual es de",descuento)#pasar esto a formula
#             print("alumno",nombre_alumno,"el valor total de su carrera es",valor_total_carrera)#pasar esto a formula
            
#     case 2:
#         if carrera2_sem>6:
#              valor_carrera_anual=(meses_semestre*2)*valor_mensual#pasar esto a formula
#              descuento=valor_carrera_anual-(valor_carrera_anual*descuento)#pasar esto a formula
#              valor_total_carrera=descuento*(carrera2_sem/2)
#              print("alumno",nombre_alumno,"su cuota anual es de",descuento)#pasar esto a formula
#              print("alumno",nombre_alumno,"el valor total de su carrera es",valor_total_carrera)#pasar esto a formula
#     case 3:
#         if carrera3_sem>6:
#             valor_carrera_anual=(meses_semestre*2)*valor_mensual#pasar esto a formula
#             descuento=valor_carrera_anual-(valor_carrera_anual*descuento)#pasar esto a formula
#             valor_total_carrera=descuento*(carrera3_sem/2)
#             print("alumno",nombre_alumno,"su cuota anual es de",descuento)#pasar esto a formula
#             print("alumno",nombre_alumno,"el valor total de su carrera es",valor_total_carrera)#pasar esto a formula
#     case _:
#         print("opcion no valida")