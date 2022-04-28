# Ejercicio 4
# Escribir un programa que solicite al usuario una letra e indique 
# si es vocal o consonante. Se debe validar que el usuario ingrese 
# solo una letra; si ingresa más de una, informar que no se puede 
# procesar el dato.

letra = (input("\nIngrese una letra: "))
longitud = len(letra)

if longitud == 1:
    letra = letra.lower()
    if letra in ("a", "e", "i", "o", "u"):
        print("La letra es una vocal.\n")
    else:
        print("La letra es una consonante.\n")
else:
    print("Ha ingresado más de una letra.")