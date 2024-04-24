#cada cucharada me quita 25% / != es distinto de/ tengo que cerrar las formula repitiendo el nombre de la formula
def cena():
    comida=100
    while comida !=0:
        print("desea comer?")
        comer=input()
        if comer=="si":
         print("cuanto desea comer?")
         cantidad_comer=int(input())
         comida=comida-cantidad_comer
         print("cantidad comida es", comida)
        else:
         print("usted ya no quiere comer")
         comida=0
        
    print("comida acabada")
cena()