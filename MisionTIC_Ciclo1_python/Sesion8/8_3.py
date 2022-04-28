# Ejercicio 3:
# Construya un script que indique si es fin de semana o no 
# al digitar uno de los dias de la semana

dia = input("\nDigite un día de la semana: ")
dia = dia.lower();
if dia in ("sabado", "domingo"):
    print("Si, es fin de semana\n")
# elif dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or dia == "viernes":
elif dia in ("lunes", "martes", "miercoles", "jueves", "viernes"):
    print("No, lamentablemente no es fin de semana\n")
else:
    print("No has digitado un dia válido...\n")