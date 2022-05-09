# Ejemplo 5
# Realice un script que evalúe la siguiente ecuación:
#   y = X^2
# Considere que x toma valores de 1 a 10.


for i in range (1, 11):
    y = i**2
    print("Resultado",i,"es igual a: ",y)

# Solución con lista:
lista=[]
for i in range (1, 11):
    lista.append(i**2)
print("\n El Resultado como lista, es igual a: ",lista)