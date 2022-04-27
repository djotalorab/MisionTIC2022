# Ejemplo 1
# Una sala de juegos cobra $5000 sie el cliente es menor de edad y 
# $10000 su supera los 18 años.
# Además, si es un niño menor de 4 años, su entrada es gratis.
# Elabore un programa que solicite la edad del cliente y arroje el 
# valor de su entrada.

edad = float(input("\nDigite la edad del cliente: "))
if edad > 0:
    if edad < 18:
        if edad < 4:
            print("La entrada es gratis para los menores de 4 años\n")
        else:
            print("La entrada cuesta $5000\n")
    else:
        print("La entrada cuesta $10000\n")