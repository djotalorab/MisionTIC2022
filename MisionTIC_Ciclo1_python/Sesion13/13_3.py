# Ejercicio 3:
# Construya un script que solicite al usuario una contraseña. 
# Si no es correcta, volver a preguntar la clave hasta que acierte

claveBien = "Zapato"
claveUsuario=input("\nDigite su contraseña: ")
while claveUsuario != claveBien:
    claveUsuario = input("Contraseña Incorrecta, digite de nuevo: ")
print("Contraseña correcta\n ")