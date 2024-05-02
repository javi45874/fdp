def suma(num1, num2):
    resul=num1+num2
    return resul
def resta(num1, num2):
    resul=num1-num2
    return resul
def multi(num1, num2):
    resul=num1*num2
    return resul
def divi(num1, num2):
    resul=num1/num2
    return resul 
def area_cuadrado(lado):
    area=lado*lado
    return area
def area_triangulo(base,altura):
    areaT=(base*altura)/2
    return areaT
def area_circulo(num):
    pi=3.14
    area=pi*(num*num)
    return area
def perimetro_circulo(num):
    pi=3.14
    peri=pi*2*num
    return peri

stay=True

while stay:
    print("Seleccione una opcion")
    print("1.- -Suma")
    print("2.- -Resta")
    print("3.- -Multiplicacion")
    print("4.- -Division")
    print("5.- -Area del cuadrado")
    print("6.- -Area del triangulo")
    print("7.- -Area del circulo")
    print("8.- -Perimetro del circulo")
    print("9.- -salir del menu")
    op=int(input())

    match op:
        case 1:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",suma(num1,num2))
        case 2:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",resta(num1,num2))
        case 3:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",multi(num1,num2))
        case 4:
            print("Ingrese 2 numeros")
            num1=int(input())
            num2=int(input())
            print("Su resultado es ",divi(num1,num2))
        case 5: 
            print("ingrese lado del cuadrado")
            lado=int(input())
            print("el area del cuadrado es",area_cuadrado(lado))
        case 6: 
            print("ingrese la base del triangulo")
            base=int(input())
            print("ingrese la altura del triangulo")
            altura=int(input())
            print("el area del triangulo es",area_triangulo(base,altura))
        case 7: 
            print("ingrese el radio del circulo")
            radio=int(input())
            print("el area del circulo es",area_circulo(radio))
        case 8: 
            print("ingrese el perimetro del circulo")
            radio=int(input())
            print("el perimetro del circulo es",perimetro_circulo(radio))
        case 9: 
            stay=False
            print("programa finalizado")


