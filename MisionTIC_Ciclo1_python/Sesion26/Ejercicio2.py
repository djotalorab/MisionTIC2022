# Ejercicio 2:
# La siguiente  estructura de datos guarda el nombre, 
# la edad y el semestre en el que se encuentra un estudiante universitario. 
# La clave es el código del alumno
#
# PAra el ejemplo, la clave es el código del estudiante y el dato contenido es una lista con el nombre, edad y semestre del alumno
# 
#    estudiantes = {2837:['Maria Salcedo', 18, 3], 1820:['Carlos Bentrán', 18, 4], 
#                   9152:['Samuel Niño', 23,8], 6103:['Julio Castro', 21, 8],
#                   4792:['Doris Bolívar', 23, 5], 3262:['Sandra Castillo', 25, 7], 
#                   7910:["Cristina García", 23, 6], 1092:["Ramón Luna", 17, 1]} 
# 
#  - Escriba un código que calcule la edad promedio de los estudiantes.
#  - Modifique el código anterior para determinar la edad promedio de 
#    los alumnos que hayan superado la mitad de su carrera.

estudiantes = {2837:['Maria Salcedo', 18, 3], 1820:['Carlos Bentrán', 18, 4], 
                9152:['Samuel Niño', 23,8], 6103:['Julio Castro', 21, 8],
                4792:['Doris Bolívar', 23, 5], 3262:['Sandra Castillo', 25, 7], 
                7910:["Cristina García", 23, 6], 1092:["Ramón Luna", 17, 1]} 

# Acumulador:
suma = 0
contador = 0

#Recorriendo el diccionario tomando los valores
for i in estudiantes.values():
    # Suma al acumulador el dato contenido en el indice 1 de la lista i
    suma += i[1]
    contador += 1
print("\nLa edad promedio de los estudiantes es: ", suma/contador, "años.\n")

contador = 0
suma = 0
for i in estudiantes.values():
    if i[2] > 5:
        suma += i[1]
        contador += 1
print("\nLa edad promedio de los estudiantes que han cursado más de la mitad de su carrera es: ", suma/contador, "años.\n")