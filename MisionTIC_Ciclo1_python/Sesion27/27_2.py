import json

def volumen(diametro, altura):
    volumen = (3.141592/4)*diametro**2*altura
    return volumen

# Importando archivos .json
# open("_NOMBREARCHIVO.json_","w") as _NOMBREVARIABLE_ (común f)
with open("dimensiones.json") as f:
    #_DICCIONARIOIMPORTADO_ = json.load(f)
    datos=json.load(f)

print(datos)
print("")

for i in datos["Dimensiones"]:
    print(i)

k=0
resultado=[]

for i in datos["Dimensiones"]:
    print(i["diametro"])
print("")

for i in datos["Dimensiones"]:
    diametro=i["diametro"]
    altura=i["altura"]
    resultado.append(volumen(diametro, altura))
    print("El volumen del recipiente", k+1, "es", resultado[k], "m3.")
    k += 1
print("")
print(resultado)
print("")