#las comillas son para representar texto

# datos = """archivo de texto simple que estoy usando de ejemplo para entender este archivo,
# """

# with open ('archivo_javi.txt','w') as archivo:#aqui cree el archivo
#     archivo.write (datos)
import random
from datetime import datetime
now=datetime.now()
tiempo=now.strftime("%Y%M%d_%H%M%S")
num=random.randint(1,10)

bingo=[]
for i in range(6):
    bingo.append(random.randint(1,50))
    print (i)
# lista="el numero del dia es", str(num)
# with open(f'listaN_javi_{tiempo}.txt','w') as archivo:
#     archivo.write (str(lista))