# Ejercicio 1:
# Una empresa elabora depósitos de acero inoxidable para almacenar leche. 
# El costo del recipiente depende de su capacidad:

# Costo = 0,25V^(0.37) [=] Miles de USD.

# Donde V es el volumen del depósito en m3. Si el peso del equipo sobrepasa 
# los 1000kg, el costo se incrementa en USD 500. La densidad del acero es: 
# 7850kg / m3. 
# Asi mismo, si el costo final sobrepasa los $ 1000, se cobra un impuesto 
# del 15% sobre el valor. Elabora un codigo que solicite al usuario las 
# dimensiones del recipiente (diámetro y altura) y arroje como resultado el 
# costo final a pagar.

import math

diametro = float(input("\nIngrese el diametro del tanque en metros: "))
altura = float(input("Ingrese la altura del tanque en metros: "))
radio = diametro/2
volumenCil = math.pi*radio**2*altura
costo = 0.25*volumenCil**0.37
masa = volumenCil*7850
if masa > 1000:
    costo += 0.5 #Miles de dolares 0,5 * 1000usd = 500usd
if costo > 1: #Miles de dolares 1 * 1000usd = 1000usd
    costo *= 1.15
print("El costo total a pagar es: $", "{:.2f}".format(costo), "x mil USD")