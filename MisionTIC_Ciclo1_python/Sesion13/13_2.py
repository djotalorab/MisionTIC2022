# Ejercicio 2:
# Elabore un código que pregunte números al usuario; 
# si la persona digita el cero, mostrar la cantidad de números 
# positivos que fueron ingresados y finalizar el código

numero = float(input("\nIngrese un número: "))
positivos = 0
while numero != 0:
    if numero > 0:
        positivos += 1
    numero = float(input("Ingrese otro número: "))
print("\nIngresó",positivos,"números positivos\n")
