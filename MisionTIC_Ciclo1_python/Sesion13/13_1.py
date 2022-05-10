# Bucles While:
# Ejemplos:
print("\nEjemplos:")
print("\n1:")

i=0
while i<10:
    print(i, end=" ")
    i+=1

print("\n\n2:")
modoInfinito = int(input("Ingrese 1 para entrar en bucle infito:"))
if modoInfinito == 1:
    while True:
        print("\n Debes reiniciar la consola!!!!!")
print("\nEjercicio 1: ")

# Ejercicio 1:
# Construya un programa que pregunte al usuario una y otra vez si desea continuar con el 
# programa siempre que responda si

desicion = input("¿Desea continuar con el programa?: ")
desicion = desicion.lower()
while desicion == "si" or desicion == "sí" or desicion == "s":
    desicion = input("¿Desea continuar con el programa?: ")
print("Hasta luego \n")