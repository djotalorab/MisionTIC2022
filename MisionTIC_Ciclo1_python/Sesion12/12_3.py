# Ejercicio 3:
# Realice un script que evalúe la siguiente ecuación:
# 
# y = x^2.
#
# Considere que x toma valores del 1 al 10. Al ejecutar el programa, 
# debe mostrar los valores de 'y' que sean un número par.

for x in range (1, 11):
    y = x**2
    if (y % 2) == 0:
        print("Resultado",x,"es igual a: ",y)
print("\nEl ultimo resultado fue: ",y,"\n")

# como lista:

lista=[]
contador = 0
for x in range (1, 11):
    lista.append(x**2)
    if (lista[contador] % 2) == 0:
        print("Resultado",x,"es igual a: ",lista[contador])
    contador += 1
print("\nEl ultimo resultado fue: ",y)