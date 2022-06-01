numeroPaquetes = int(input())
costoTotal = 0
for i in range (1, numeroPaquetes+1):
    alto = float(input())
    ancho = float(input())
    profundo = float(input())
    volumen = alto*ancho*profundo
    costo = volumen*5
    if alto > 30:
        costo += 2000
    if costo > 10000:
        costo *= 1.19
    print("{:.1f}".format(volumen))
    print("{:.1f}".format(costo))
    costoTotal += costo
print("{:.1f}".format(costoTotal))


