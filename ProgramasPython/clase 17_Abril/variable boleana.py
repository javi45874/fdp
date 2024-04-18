##EJEMPLO TICKET:
# ticket_valido=False
# folio_valido=123

# print("ingrese el numero de folio")
# n_folio=int(input())

# if n_folio==folio_valido:
#     ticket_valido=True

# if ticket_valido:
#     print("ticket valido")
# else:
#     print("ticket caducado")

### Ejemplo and/or
edad=9
grupo="A"

if edad>=18 or grupo=="A":
    print("usted es mayor y pertenece al grupo A")

elif edad>=18 and grupo=="B":
    print("usted es mayor, y pertenece al grupo B")
else:
    print("no se cumplio la edad o grupo")