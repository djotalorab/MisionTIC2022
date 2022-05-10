# Ejercicio 5:
# Diseñe un código que calcule el factorial de un número entero (use unicamente la sentencia while).

numero = int(input("\nDigite el número al que desea calcular su factorial: "))
contador = 0

while numero < 0:
    print("\nEl factorial de un número negativo, no existe:")
    numero=int(input("Digite otro número \n"))

factorial = 1
k=2

while numero >= k:
    factorial *= k
    k+=1
print("\nEl factorial de", numero, "es:", factorial)