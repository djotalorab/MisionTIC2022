
# Condicionales:

# Ejemplos:
# Realizar un código que compruebe si el número ingresado por el usuario es par.

numero = float(input("\nDigite el número para averiguar si es par... "))
residuo = numero % 2
if residuo == 0:
    print("El número es par. ")
else:
    print("El número es impar")

# Ejercicio 1:
# Ejecute un Script que solicite al usuario su edad y 
# muestre si es mayor de edad.

edad = float(input("\nDigite su edad: "))
if edad < 0:
    edad=float(input("La edad no puede ser negativa, digite nuevamente: "))
if edad >=18:
    print("Usted es mayor de edad\n")
else:
    print("Usted es menor de edad\n")


# Ejercicio 2:
# Escriba un programa que pida al usuario una contraseña y 
# defina si es o no correcta

password = input("\nDigite su clave ")
frase_maestra = "ABC123ABC"
if password == frase_maestra:
    print("Contraseña correcta \n")
else:
    print("Contraseña incorrecta\n")


# Ejercicio 3
# construya un srcipt que pida al usuario dos números y muestre el 
# resultado de su división. El script debe considerar que el denominador 
# no pude ser cero.

numerador = float(input("\nEscriba el numerador. "))
denominador = float(input("Escriba el denominador. "))
if denominador == 0:
    denominador = float(input("El denominador no puede ser cero, escribalo nuemavamente: "))
resultado = numerador / denominador
print("El resultado de su división es: ", "{:.3f}".format(resultado))


# Ejercicio 4
# construya un código que pida al usuario dos números y muestre cual digito 
# es mayor. No emplee los operadores de comparación mayor que (>) y menor 
# que (<)

numero1 = float(input("\nDigite el primer numero a evaluar: "))
numero2 = float(input("Digite el segundo número: "))
if numero2 != 0:
    division = numero1 / numero2
    if division > 1:
        print(numero1, " Es mayor que ", numero2)
    if division < 1:
        print(numero2, " Es mayor que ", numero1)
    if division == 1:
        print("Los numeros son iguales")
if numero2 == 0:
    print(numero1, " Es mayor que ", numero2)