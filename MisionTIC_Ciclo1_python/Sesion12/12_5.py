# Ejercicio 6:
# Escriba un programa que solicite al usuario una frase y al ejecutarlo, 
# muestre el número total de letras
# prueba: Hola Mundo    Resultado: 9
# Prueba: La Pelota De Ellos    Resultado: 15
# Prueba: Buenas noches     Resultado: 12

frase = input("\nIngrese una frase: ")
letras = 0
for letra in frase:
    if letra != " ":
        letras += 1
print("\nModo 1: En la frase hay",letras,"letras")

# Otro modo:

letras = 0
for letra in frase:
    if letra == " ":
        continue    
    letras += 1
print("Modo 2: En la frase hay",letras,"letras\n")