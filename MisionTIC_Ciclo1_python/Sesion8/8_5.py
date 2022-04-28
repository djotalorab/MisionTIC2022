# Ejercicio 5:
# Elabore un script que permita saber si un año es bisiesto. 
# Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, 
# exepto que también sea divisible por 400.

anio = int(input("\nDigite un año: "))
siesbi = "Es un año bisiesto\n"
noesbi = "No es un año bisiesto\n"
if anio % 4 == 0:
    if anio % 100 != 0:
        print(anio, siesbi)
    elif anio % 400 == 0:
        print(anio, siesbi)
    else:
        print(anio, noesbi)
else:
    print(anio, noesbi)