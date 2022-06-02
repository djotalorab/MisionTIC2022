import json

with open("paquetes.json") as f:
    listaPaquetes = json.load(f)
    print("")
    print(listaPaquetes)
    print("Diccionario 'paquetes' creado\n")



def calcularCosto(alto, ancho, profundo):
    volumen = alto*ancho*profundo
    costo = volumen*5
    if alto > 30:
        costo += 2000
    if costo > 10000:
        costo *= 1.19
    return costo

def costoTotal(listaPaquetes, descuento):
    costoTotal = 0
    for i in listaPaquetes["PAQUETES"]:
        alto = i["ALTO"]
        ancho = i["ANCHO"]
        profundo = i["PROFUNDO"]     
        costoTotal += calcularCosto(alto, ancho, profundo)
    return costoTotal*(1-descuento/100)

print(costoTotal(listaPaquetes, 50))
    