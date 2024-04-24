#contar las micros, hasta las 12 del dia, empiezo a las 8, si digo que no pasa 1 hora (tengo 3 intentos), si digo que si suma 1micro
def contador_micros():
  cant_micros=0
  hora=8

  while cant_micros !=3 and hora !=12:
     print("ha pasado una micro?")
     respuesta=input()
     if respuesta=="si":
            cant_micros=cant_micros+1
            print("han pasado ", cant_micros,"micros")
            if cant_micros==3:
             print("ya no pasaran mas micros")
     if respuesta=="no":
            hora=hora+1
            print("la hora es", hora)
            if hora==12:
                print("horario finalizado")

  print("terminado")  

contador_micros()  