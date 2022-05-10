# Ejemplo 10
# Realice un programa que pida al usuario dos números. 
# Luego, debe solicitar un tercer número que represente la operación 
# matemática que desee hacer 
# (1 Suma, 2 Resta, 3 Multiplicación, 4 División) y mostrar el resultado.

primerOperador = float(input("\nDigite el primer operador: "))
segundoOperador = float(input("Digite el segundo operador: "))
opcion = int(input("\n¿Que operación desea realizar? 1 para suma, 2 para resta, 3 para multiplicación y 4 para división: "))

if opcion in (1,2,3,4):
    if opcion == 1:
        print("El resultado de la suma es: ","{:.2f}".format(primerOperador + segundoOperador),"\n")
    elif opcion == 2:
        print("El resultado de la resta es: ","{:.2f}".format(primerOperador - segundoOperador),"\n")
    elif opcion == 3:
        print("El resultado de la multiplicación es: ","{:.2f}".format(primerOperador * segundoOperador),"\n")
    else:
        if segundoOperador != 0:
            print("El resultado de la división es: ","{:.2f}".format(primerOperador / segundoOperador),"\n")
        else:
            print("No es posible dividir entre cero...\n")
else:
    print("Digite una opción válida \n")