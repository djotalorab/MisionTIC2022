# Ejemplo 6
# Construlla un código que calcule el resultado de la siguiente sumatoria:
# (n)(sumatoria)(i=1) (m)(sumatoria)(j=1) (i^2 * j)
# Donde, n y m, son enteros

n = int(input("\nIngrese el valor final de la primera sumatoria: "))
m = int(input("Ingrese el valor final de la segunda sumatoria: "))
print("")
sumatoria = 0
for i in range (1, n+1):
    for j in range (1, m+1):
        sumatoria += i**2 * j
        print(sumatoria)
print("\nEl valor de la sumatoria es: ",sumatoria)