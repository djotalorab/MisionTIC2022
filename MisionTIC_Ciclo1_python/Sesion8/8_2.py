# Ejemplo 2:
# Escriba un programa que, al ejecutar, solicite tres números e 
# identifique cuál valor es el menor.

numero1 = float(input("\nDigite el primer número: "))
numero2 = float(input("Digite el segundo número: "))
numero3 = float(input("Digite el tercer número: "))
if numero1 < numero2 and numero1 < numero3:
    print("El número menor el es el primer número: ", numero1, "\n")
elif numero2 < numero1 and numero2 < numero3:
    print("El número menor el es el segundo número: ", numero2, "\n")
else:
    print("El número menor el es el tercer número: ", numero3, "\n")