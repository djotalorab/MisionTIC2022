# Ejercicio 2:
# Elabore un script que compute la suma de los números pares entre 1 y N, 
# donde N e un entero. En el mismo código realice la suma de los números impares.

N = int(input("\nIngrese un número entero: "))
sumaPares = 0
for i in range(2, N+1, 2): # (DESDE 2, HASTA N+1, DE 2 EN 2)
    sumaPares += i
print("\nLa suma de los números pares es:", sumaPares)
sumaImpares = 0
for i in range(1, N+1, 2): # (DESDE 1, HASTA N+1, DE 2 EN 2)
    sumaImpares += i
print("La suma de los números impares es:", sumaImpares,"\n")