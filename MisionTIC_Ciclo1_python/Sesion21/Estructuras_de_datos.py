# Las estructuras de datos (contenedores) son variables que funcionan como contenedores; 
# es decir,, guardan más de un elemento. Sirven para dar solución más eficiente a 
# ciertos problemas, por ejemplo: manejo de calificaciones, gestión de nómina, etc.

# Listas: Son estructuras de datos formadas por una secuencia ordenada de objetos. 
# Los elementos de una lista pueden accederse mediante su indice, siendo 0 (cero) 
# el indice del primer elemento.
#  Características de una lista: 
#   -Elementos ordenados por indice:
#   - Puede tener elementos repetidos
#   - Se pueden constituir por elementos heterogeneos.
#   - Son estructuras mutables, es decir, puede cambiar su contenido.
# 
# Lista = [1,2,3,4,5] = [1, 2, 3, 4, 5]
# Lista2 = list(range(1,6)) = [1, 2, 3, 4, 5]
# 
# Las listas se recorren con ciclos for y while:
# for i in range(len(lista1)):
#       print(lista1[i])
# 
# while i < len(lista1):
#       print(lista1[i])
#       i += 1

lista1 = [0, 1, 2, 3, 4]
lista2 = [5, 6, 7, 8, 9]

#suma dos listas en lista 3
lista3 = lista1 + lista2
print("\n", lista3)

#modifica Elementos específicos (indice)
lista3[0] = 1
lista3[5] = 10
print("\n",lista3)

# Devuelve la posición del primer elemento n (index(n)) 
# dentro de la lista antes del punto. 
# Para el ejemplo, buscará la posición del elemento 1 dentro de lista3
print("\n", lista3.index(1))

# Averiguar si un valor específico está en la lista, devuelve true or false
print("\n" ,10 in lista3)

# Cuenta el número de veces que se repite un elemento en la lista
print("\n", lista3.count(1))

# Agregar elementos al final de la lista con append
lista3.append(11)
lista3.append(12)
print("\n", lista3)

# Agregar elementos en una posición específica con insert.
lista3.insert(0, 0)
lista3.insert(0, -1)
print("\n", lista3)

# Agregar una lista como elemento de otra lista.
# Agrega como lista, como un unico elemento en la lista nueva.
lista3 = lista1 + lista2
print("\n", lista3)
lista3.append(lista1)
print(lista3)

# Agregar los elementos de una lista como elementos de otra
# Sin corchetes, como elementos independientes.
lista3 = lista1 + lista2
print("\n", lista3)
lista3.extend(lista1)
print(lista3)

# Para buscar y remover un elemento dentro de la lista:
# Buscará el elemento n dentro de remove(n) y  eliminará
# la primera coincidencia.
print("\n", lista3)
lista3.remove(4)
print(lista3)

# Para eliminar un elemento dentro de un indice específico.
print("\n", lista3)
lista3.pop(4)
print(lista3)

# También con:
print("\n", lista3)
del lista3[2]
print(lista3)

# Para borrar una lista en su totalidad:
print("\n", lista3)
lista3.clear()
print(lista3)