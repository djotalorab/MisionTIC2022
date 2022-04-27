# Ejercicio 4
# Una institución educativa establece un apoyo económico para sus estudiantes, 
# basado en su desempeño académico y situación socioeconómica. 
# Si el estudiante tiene un promedio mayor a 3,5 y 
# pertenece al estrato 1, 2 o 3; es merecedor de una beca equivalente 
# al 100% de su matricula. 
# Elabore un script que, al digitar el promedio y el estrato del alumno, 
# defina si la persona merece o no el auxilio económico.

promedio = float(input("\nDigite el promédio académico: "))
estrato = int(input("Digite el estráto del alumno: "))
# if promedio > 3.5 and estrato <= 3:
if promedio > 3.5 and estrato in (1,2,3):
    print("\nEl alumno merece un auxilio educativo.\n")
else:
    print("\nCreemos que el alumno no merece ser apoyado.\n")