# Solicitar al usuario que ingrese su nombre
nombre = input("Por favor, ingresa tu nombre: ")

# Imprimir un saludo personalizado
print("Hola,", nombre, "! Bienvenido a Python.")
# input es como el leer de pseint, print es como el escribir

#solicitar al usuario ingresar una variable entera
variable_entera = int(input("ingrese una variable entera "))
print("valor ingresado es: ",variable_entera)

#solicitar al usuario ingresar una variable decimal
variable_decimal = float(input("ingrese una variable decimal "))
print("valor ingresado es: ",variable_decimal)

resultado_suma=variable_decimal+variable_entera
print("valor suma es",resultado_suma)

promedio_datos= resultado_suma/2
print("promedio de los valores es: ", promedio_datos)