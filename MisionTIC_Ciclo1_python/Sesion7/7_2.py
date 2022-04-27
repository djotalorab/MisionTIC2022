# Ejemplo 2
# EL impuesto sobre la renta en un determinado pais de la Unión Europea
# depende del ingreso anual del ciudadano.
#
#   Renta anual:    Impuesto %
#   x < 10000           5
#   10k<= x <20k        15
#   20k<= x < 35k       20
#   35k<= x < 60K       30
#   60000 < X           45
# 
# Elabore un script que pregunte al usuario su renta y calcule el valor del 
# impuesto que debe pagar

renta = float(input("\nIngrese su renta anual: "))
if renta < 10000:
    impuesto = (renta * 0.05)
    print("Le corresponde pagar una renta de: ","{:.2f}".format(impuesto),"euros\n")
elif renta < 20000:
    impuesto = (renta * 0.15)
    print("Le corresponde pagar una renta de: ","{:.2f}".format(impuesto),"euros\n")
elif renta < 35000:
    impuesto = (renta * 0.20)
    print("Le corresponde pagar una renta de: ","{:.2f}".format(impuesto),"euros\n")
elif renta < 60000:
    impuesto = (renta * 0.30)
    print("Le corresponde pagar una renta de: ","{:.2f}".format(impuesto),"euros\n")
else:
    impuesto = (renta * 0.45)
    print("Le corresponde pagar una renta de: ","{:.2f}".format(impuesto),"euros\n")