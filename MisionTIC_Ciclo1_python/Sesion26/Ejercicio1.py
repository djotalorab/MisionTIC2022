#Ejemplo 1:
# Escriba un código que muestre cuantas veces se 
# repite cada letra que compone una frase dada por el usuario

alfabeto = "aábcdeéfghiíjklmnñoópqrstuúvwxyz"
diccionario = {}

# Llena el diccionario creando una clave con cada caracter del string alfabeto
for i in alfabeto:
    diccionario[i]=0

frase = input("\nEscriba una frase: ").lower()
# Recorre la frase guardada tomando copiando el valor de cada letra del string en la variable "j":
for j in frase:
    # Si la letra se encuentra dentro del string 'alfabeto', ignora los simbolos, espacios etc:
    if j in alfabeto:
        # Suma 1 al dato contenido en la clave "j" del diccionario
        diccionario[j]+=1

# Recorre el diccionario copiando en 'letra' las claves y en 'cantidad' los datos:
# for [claves], [datos] in diccionario.items():
for letra, cantidad in diccionario.items():
    # Si el dato es mayor que cero (Si el valor contenido en la clave es mayor a cero)
    if cantidad > 0:
        # muestra la clave y la cantidad
        print(letra, ":", cantidad)
