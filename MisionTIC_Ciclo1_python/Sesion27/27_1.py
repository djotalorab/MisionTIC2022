# Exportando los datos a .json

# Importando librería json
import json

# Creación de un diccionario que contiene una clave con una lista que a su vez contiene 3 diccionarios. ....
recipiente1 = {"diametro":0.5, "altura":3}
recipiente2 = {"diametro":1, "altura":4}
recipiente3 = {"diametro":1.5, "altura":5}

datos = {}
datos['Dimensiones']=[]
# Lo anterior es igual a: datos = {'Dimensiones':[]}

# Se agrega el diccionario 'recipiente1' a la lista correspondiente 
# al valor de la clave 'Dimensiones' del diccionario datos
datos["Dimensiones"].append(recipiente1)

datos["Dimensiones"].append(recipiente2)
datos["Dimensiones"].append(recipiente3)
print("\n",datos,"\n")

# Creación del archivo texto de destino
# open("_NOMBREARCHIVO.json_","w") as _NOMBREVARIABLE_ (común f)
with open("dimensiones.json","w") as f:
    # json.dump(_DICCIONARIOAEXPORTAR_ , _NOMBREVARIABLE_)
    json.dump(datos,f)

with open("dimensiones.txt","w") as f:
    json.dump(datos,f)
