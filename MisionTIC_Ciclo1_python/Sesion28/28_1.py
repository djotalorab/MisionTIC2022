# Ejercicio tipo reto.
import json

with open("dimensiones.json") as f:
    datos = json.load(f)
    print("")
    print(datos)
    print("Diccionario 'datos' creado\n")

def costo_unitario(diametro, altura):
    volumen = (3.1416/4)*diametro**2*altura
    costo = 250*volumen**0.37
    peso = 7850*volumen
    if peso > 1000:
        costo += 500
    if costo > 1000:
        costo *= 1.15
    return costo

def costo_total(datos, descuento):
    total = 0
    for i in datos["Dimensiones"]:
        diametro = i["diametro"]
        altura = i["altura"]
        total += costo_unitario(diametro, altura)
    return total*(1-descuento/100)

print(costo_total(datos,30),"\n")
