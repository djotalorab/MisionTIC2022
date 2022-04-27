# Ejemplo 5:
# El contexto señalado en el ejercicio anterior puede ser un poco injusto. 
# Por lo tanto, las directivas del centro educativo establecieron que, 
# si el estudiante cumple alguna de las dos condiciones, recibe el 50% de la beca. 
# Escriba un código que determine si el alumno merece la beca y el porcentaje de la misma.

promedio = float(input("\nDigite el promédio académico: "))
estrato = int(input("Digite el estráto del alumno: "))
# if promedio > 3.5 and estrato <= 3:
if promedio > 3.5 and estrato in (1,2,3):
    print("\nEl alumno merece un auxilio educativo.\n")
elif promedio > 3.5 or estrato in (1,2,3):
    print("\nEl alumno merece el 50% de auxilio educativo.\n")
else:
    print("\nLamentablemente el alumno no merece ser apoyado.\n")