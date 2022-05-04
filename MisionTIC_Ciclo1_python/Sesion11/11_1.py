# Ejercicio 1
# Dado un número natural 'n', se quiere sumar los cubos de los 
# números de 1 hasta 'n'. Elabore un código que arroje el resultado.

N = int(input("\nIngrese un número entero: "))
print("")
suma = 0
for i in range (1, N+1):
    suma += i**3
    print("\t",suma)
print("\nEl resultado de la suma es: ", suma,"\n")