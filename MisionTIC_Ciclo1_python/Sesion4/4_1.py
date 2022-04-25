# Ejercicio 9
# La temperatura del sol es, aproximadamente, 5500°C. Escriba un código que arroje
# el valor de la temperatura en grados Fahrenheit. 
# La respuesta no debe contener decimales e indicar la separación de millares.
# °F = 1,8°C + 32

temperatura = 5500
fahrenheit = 1.8*temperatura+32
print("\nLa temperatura del sol en fahrenheit es: ", "{:,.0f}".format(fahrenheit), "°f \n")


# Ejercicio 10
# Elabore un script que al ejecutarlo, solicite al usuario su nombre y devuelva la 
# cantidad de letras que lo componen, a demas de su inicial.

nombre = input("Digite su nombre completo: ")
palabras = int(input("Digite la cantidad de palabras que componen su nombre: "))

tamanio = int(len(nombre)-(palabras-1))
print("La longitud de su nombre es: ", tamanio, " letras")
print("La inicial de su nombre es la letra: ", nombre[0])
# string.upper() cambia todo a MAYúSCULA
# string.lower() cambia todo a minúscula
# string.title() Pone La Primera Letra De Cada Palabra En Mayúscula


# Ejercicio 11
# ¿Cómo escribiría en Python la siguiente operación aritmética para que se ejecute correctamente?:
# ((5+7)/6)^^4

operacion = ((5+7)/6)**4
print("\nLa operación del ejercicio 11, debería dar 16 y da:... ", operacion)


# Ejercicio 12
# Construya un código que solicite al usuario una fecha formada por 8 números (DDMMAAAA) 
# y devuelva el resultado en formato DD/MM/AAA

fecha = input("\nDigite el número que representa la fecha: ")
print("La fecha es: ", fecha[0:2],"/", fecha[2:4],"/", fecha[4:])


# Ejercicio 13
# Realizar un código que compruebe si el número ingresado por el usuario es par.

numero = float(input("\nDigite el número para averiguar si es par... "))
residuo = numero % 2
print(residuo==0)


# Ejercicio 14
# Realizar un código que calcule el indice de masa corporal del usuario.
# IMC = Masa/estatura^2  masa en kilogramos, estatura en metros

masa = float(input("\nDigite su peso en kilogramos: "))
altura = float(input("Digite su altura en metros: "))
imc = masa/altura**2
print("Su indice de masa corporal es: ","{:.1f}".format(imc), "%\n")