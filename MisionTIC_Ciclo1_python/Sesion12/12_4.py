# Ejemplo 9:
# Escriba un programa que le solicite al usuario una clave y arroje si es o no correcta:
#
# Clave = 1357
# claveUsuario = int(input("\nDigite la contraseña: "))
# if claveUsuario == Clave:
#     print("\nClave válida\n")
# else:
#     print("\nClave inválida\n")
# Modo dificil:

clave = "GrupoA"
contrasenia = input("\nDigite la constraseña: ")
contador = 0
resultado = True
for i in contrasenia:
    if i != clave[contador]:
        resultado = False
        break   
    contador += 1
if resultado:
    print("\nSu contraseña es correcta\n")
else:
    print("\nSu constraseña es incorrecta\n")