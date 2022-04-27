# Ejemplo 3:
# En Colombia todo ciudadano debe declarar renta si:
#   
#   - El patrimonio bruto al término del año gravable 2021 sea 
#   igual o superior a $163386000
#   - Los ingresos totales del respectivo ejercicio gravable 
#   sean iguales o superiores a $50831000
#   - Los consumos mediante tarjeta de crédito sea iguales o 
#   superiores a $50831000
#   - El valor total de las compras y consumos sean igual o 
#   superior a $50831000
#   - El valor total acumulado de consignaciones bancarias, 
#   depositos o inversiones financieras, sean iguales o 
#   supeiores a $50831000
#
# Elabore un código que muestre como resultado si el usuario debe o no declarar renta.

patrimonio = float(input("\nDigite su patrimonio bruto al término del año gravable: "))
ingresos_totales = float(input("Digite los ingresos totales del respectivo ejercicio gravable: "))
consumos_tarjeta = float(input("Digite el total de las compras con tarjeta de crédito al año gravable: "))
compras_y_consummos = float(input("Digite las compras y consumos del año gravable: "))
consignaciones_depositos_inversiones = float(input("Digite el total de las consignaciones, depositos e inversiones financieras al año gravable: "))
tope_patrimonio = 163386000
tope_bancarios = 50831000
if patrimonio >= tope_patrimonio or ingresos_totales >= tope_bancarios or consumos_tarjeta >= tope_bancarios or compras_y_consummos >= tope_bancarios or consignaciones_depositos_inversiones >= tope_bancarios:
    print("\nLamentablemente deberá declarar renta para este año gravable.\n")
else:
    print("\nExcelente, no deberá declarar renta este año.\n")