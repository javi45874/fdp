import requests
import json
import pandas as pd
url= "https://jsonpacleholder.typicode.com/todos";
response=requests.get(url)
if response.status_code==200:
    guardar=open("todo.json","w")
    guardar.write(response.text);
guardar.close()
df=pd.read_json