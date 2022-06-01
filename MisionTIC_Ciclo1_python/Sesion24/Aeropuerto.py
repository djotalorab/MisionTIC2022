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

datos = []
while True:
    print("\n1. Agregar Datos")
    print("2. Buscar Ciudad de destino")
    print("3. Número de pasajeros con destino a una determinada ciudad")
    print("4. Visualizar la base de datos.")
    print("5. Salir")
    opcion = int(input("Digite la opción escogida: "))

    if opcion == 1:
        numero = int(input("\nIngrese el número de viajeros: "))
        contador = 0
        while contador < numero:
            print("\n\tPasajero número:", contador+1)
            nombre = input("\tIngrese el nombre del viajero: ")
            nombre = nombre.lower()
            cedula = int(input("\tIngrese la cédula del viajero: "))
            origen = input("\tIngrese el origen del viajero: ")
            origen = origen.lower()
            destino = input("\tIngrese el destino del viajero: ")
            destino = destino.lower()
            datos.append((nombre, cedula, origen, destino))
            contador+=1
    
    elif opcion == 2:
        consultaCedula = int(input("\nDigite el número de cédula a consultar:"))
        for i in datos:
            if i[1] == consultaCedula:
                print("El destino del pasajero es:", i[3], "\n")

    elif opcion == 3:
        consultaCiudad = input("\nDigite la ciudad a buscar:")
        consultaCiudad = consultaCiudad.lower()
        contadorCiudad = 0
        for i in datos:
            if i[3] == consultaCiudad:
                contadorCiudad += 1
        print(contadorCiudad, "pasajeros viajan a", consultaCiudad, "\n")

    elif opcion == 4:
        print("")
        for i in datos:
            print(i)

    elif opcion == 5:
        print("\nHasta pronto\n")
        break

    else:
        print("\nNo ha seleccionado una opción válida.")