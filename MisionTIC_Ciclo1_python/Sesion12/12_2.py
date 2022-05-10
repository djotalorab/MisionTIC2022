# Ejemplo 7:
# Escriba un programa que solicite al usuario una frease y, 
# al ejecutarlo, muestre como resultado cada una de las vocales y la cantidad total.

frase = input("\nEscriba una frase: ")
frase= frase.lower()
vocales = 0
print("\nVocales:")
for caracter in frase:
    #if caracter in ("a", "e", "i", "o", "u"):
    if caracter in "aeiou":        
        print(caracter, end=" ")
        vocales+=1
print("\nEl total de vocales en la frase es: ",vocales, "\n")