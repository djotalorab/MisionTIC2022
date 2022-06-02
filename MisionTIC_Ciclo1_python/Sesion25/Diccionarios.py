# Diccionarios:
# Son estructuras que almacenan datos mediante clave; 
# de esta forma los datos se ordenan de manera más sencilla. Son mutables
#
# Diccionario = {clave:valor}

diccionario = {"Nombre": 'Andrés', "Apellido": "Benavides", "Ciudad": "Bucaramanga", 'Profesión': 'Ingeniero'}
print(diccionario["Ciudad"])
# Con el método get obtiene el valor de una clave o arroja un mensaje en caso de no poder obtener el valor:
print(diccionario.get("Profesión", "NO hay datos en esta clave..."))
print(diccionario.get("EstadoCivil", "NO hay datos en esta clave..."))
print("")


#Ejemplo 2: El diccionario almacena valores de tipo cadena, flotantes y lista.
diccionario2 = {"Nombre": 'Daniel', "Apellido":'Otálora', "Codigo":910709, "Notas":[3.5, 4.0, 4.5]}
print(diccionario2)

# Para visualizar el valor contenido en una clave:
print(diccionario2["Nombre"])
print(diccionario2["Notas"])

# Para agregar más claves al diccionario:
diccionario2["Edad"] = 30
print(diccionario2)

# Para cambiar el valor contenido en una clave:
diccionario2["Edad"] = 69
print(diccionario2)

# Para ver cuantas claves tiene un diccionario (Análogo a len())
print(diccionario2.keys())

# Para ver los valores contenidos en todas las claves:
print(diccionario2.values())

# Para eliminar una clave de un diccionario.
# Método uno
diccionario2.pop("Edad")
print(diccionario2)

# Método dos
del(diccionario2["Codigo"])
print(diccionario2)