# Diccionarios:
# Son estructuras que almacenan datos mediante clave; 
# de esta forma los datos se ordenan de manera más sencilla. Son mutables
#
# Diccionario = {clave:valor}

diccionario = {"Nombre": 'Andrés', "Apellido": "Benavides", "Ciudad": "Bucaramanga", 'Profesión': 'Ingeniero'}
print(diccionario["Ciudad"])
# Con el mpetododo get obtiene el valor de una clave o arroja un mensaje en caso de no poder obtener el valor:
print(diccionario.get("Profesión", "NO hay datos en esta clave..."))
print(diccionario.get("EstadoCivil", "NO hay datos en esta clave..."))