# Ejemplo 6:
# Un aeropuerto desea implementar una base de datos para llevar un registro de cada viajero. 
# Para ello, plantea crear una lista de tuplasdonde cada una contenga el nombre de la persona, 
# su cédula, ciudad de origen y ciudad de destino. 
# 
# lista = [(persona1, cedula1, origen1, destino1), (persona2, cedula2, origen2, destino2)]
# 
# Elabore un código que permita al usuario cargar los datos e cada pasajero y, además, 
# consultar con el número de cédula a que ciudad viaja la persona. También considere la
# posibilidad de valorar cuántas pérsonas viajan a una ciudad específica.

numero = int(input("\nIngrese el número de viajeros: "))
contador = 0
datos = []
while contador < numero:
    print("\n\tPasajero número:", contador+1)
    nombre = input("\tIngrese el nombre del viajero: ")
    cedula = int(input("\tIngrese la cédula del viajero: "))
    origen = input("\tIngrese el origen del viajero: ")
    destino = input("\tIngrese el destino del viajero: ")
    datos.append((nombre, cedula, origen, destino))
    contador+=1

print("\n",datos)