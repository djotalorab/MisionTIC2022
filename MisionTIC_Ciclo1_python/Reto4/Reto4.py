def calcularCosto(alto, ancho, profundo):
    volumen = alto*ancho*profundo
    costo = volumen*5
    if alto > 30:
        costo += 2000
    if costo > 10000:
        costo *= 1.19
    return costo

def costoTotal(numeroPaquetes, descuento):
    costoTotal = 0
    for i in range (1, numeroPaquetes+1):
        alto = float(input())
        ancho = float(input())
        profundo = float(input())        
        costoTotal += calcularCosto(alto, ancho, profundo)
    return costoTotal*(1-descuento/100)

print(calcularCosto(35,10,5))
print(costoTotal(2, 50))
    