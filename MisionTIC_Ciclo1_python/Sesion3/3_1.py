# Ejercicio 6
# Construya un script que, al ejecutarlo, le pida al usuario dos numeros 
# (numerador y denominador) y retorne el resultado de su división, el módulo y la parte entera.

numerador = float(input("\nDigite el numerador: "))
denominador = float(input("Digite el numerador: "))
division = numerador / denominador
modulo = numerador % denominador
parte_entera = numerador // denominador

print("\nEl resultado de la división es: ", "{:.3f}".format(division)) #Formateado a 3 digitos decimales.
print("El módulo de la división es: ", modulo)
print("La parte entera de la división es: ", parte_entera)


# Ejercicio 7
# La población de una ciudad era de 350000 personas en el año 2020. Así mismo, su creccimiento 
# poblacional se enstima por la siguiente ecuación:
# 
#  P = P(subZero) * e^(0,012 * t). 
# 
# Donde P(subZero) es su población en el año cero (2020), y t es la cantidad de años 
# transcurridos desde el año cero. 
# 
# Escriba un código que le solicite al usuario un año en particular y retorne la cantidad de 
# personas que tendrá la ciudad (sin cifras decimales).

import math

anio = float(input("\nDigite el año al cual desea proyectar su población: "))
tiempo = anio-2020
poblacion = 350000*math.exp(0.012*tiempo)
print("La población en el año ", "{:.0f}".format(anio), " será de ", "{:.0f}".format(poblacion), " habitantes\n")


# Ejercicio 8
# Un depósito cilíndrico es empleado para almacenar agua (densidad de 1000kg/m^(3)).
# Para evitar que el líquido se derrame, el tanque se llena hasta un 80% de su máxima capacidad. 
# Además, el costo del recipiente depende de su capacidad: 
# 
# Costo = 0.63V^(0,57) [=]miles de USD$ 
# 
# Donde, V es el volumen del depósito en metros cúbicos. 
# Diseñe un código que solicite al usuario las dimensiones del recipiente (diametro y altura)
# y arroje como resultado la capacidad del tanque, su costo y la masa de agua que puede contener. 
# Las respuestas deben estar dadas en sus unidades respectivas. Para la capacidad muestre 
# dos cifras decimales, una para costo y ninguna para la masa.

diametro = float(input("Ingrese el diametro del tanque en metros: "))
altura = float(input("Ingrese la altura del tanque en metros: "))
radio = diametro/2
volumenCil = math.pi*radio**2*altura
costo = 0.63*volumenCil**0.57
masa = 1000*volumenCil*0.8
print("\nLa capacidad del tanque es de: ", "{:.2f}".format(volumenCil), "m3.")
print("El costo del tanque es: $", "{:.1f}".format(costo), "mil USD")
masa = int(masa)
print("La masa maxima dentro del tanque sera de: ", "{:,}".format(masa), "kg\n")