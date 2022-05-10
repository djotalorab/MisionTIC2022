# Ejercicio 4::
# considere el ejercicio anterior y limite el número de intentos a 3.

claveBien = "Zapato"
claveUsuario=input("\nDigite su contraseña: ")
intentos = 0
resultado = True
while claveUsuario != claveBien:
    intentos += 1
    if intentos == 3:
        print("Intentos permitidos exedidos")
        resultado = False
        break        
    claveUsuario = input("Contraseña Incorrecta, digite de nuevo: ")
        
if intentos < 3:
    print("Contraseña correcta\n ")