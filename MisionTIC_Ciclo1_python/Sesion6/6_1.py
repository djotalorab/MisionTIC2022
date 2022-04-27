# Ejercicio 5
# Escriba un cógido que evalúe, con base en la edad del solicitante, 
# si se asigna o no una licencia de conducir. No es posible para menores
# de 16 años; menores de 18 tienen un permiso temporal y mayores de 70
# requieren una licencia especial.

edad=float(input("\nDigite la edad del solicitante: "))
if edad < 16:
    print("El Solicitante aun no puede tener licencia.\n")
elif edad < 18:
    print("El solicitante puede obtener un permiso temporal.\n")
elif edad < 70:
    print("Se puede expedir el permiso de conducción.\n")
else:
    print("El solicitante requiere una licencia especial por ser mayor de 70 años.\n")


# Ejercicio 6
# Elabore un script que le solicite al usuario un número y arroje si es 
# positivo o negativo.
numero = float(input("\nDigite un número: "))
if numero == 0:
    print("El cero no es negativo o positivo...\n")
elif numero > 0:
    print("El número es positivo\n")
else:
    print("El número es negativo\n")