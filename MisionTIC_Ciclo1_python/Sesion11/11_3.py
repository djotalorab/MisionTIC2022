# Ejemplo 3:
# Escriba un programa que calcule el factorial de un número.

numero = int(input("\nDigite el número al que desea calcular su factorial: "))
if numero >= 0:
    factorial = 1
    if numero == 0:
        print("El factorial es: ", factorial, "\n")
    if numero != 0:
        for i in range (1, numero+1):
            factorial *= i
            print(factorial)
        print("El factorial es: ", factorial, "\n")
else:
    print("El número no puede ser menor a cero\n")