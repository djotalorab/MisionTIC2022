departamentos = {"Cundinamarca":'Bogotá', "Antioquia":"Mierdellín", "Valle":"Cali", "Atlantico":"Barranquila"}
# Muestra las claves:
for i in departamentos:
    print(i)
print("")

# Muestra los datos contenidos en las claves: (En este caso, i toma el valor de la clave)
for i in departamentos:
    print(departamentos[i])
print("")

# Muestra los datos contenidos en las claves: (En este caso, i toma el valor del dato)
for i in departamentos.values():
    print(i)
print("")
# Muestra los datos contenidos en las claves: (En este caso, i puede tomar el valor de la clave o el dato [0][1])
for i in departamentos.items():
    print(i[0])
    print(i[1])
print("")
for i,j in departamentos.items():
    print(i)
    print(j)
print("")