# Ejercicio 4
# Elaborar un código para realizar el calculo de la siguiente sumatoria:
#   (100(SUM)i=1)((i^2)*sen((i^2)+(3*PI))*(i*cos(pi/i)))
import math
sumatoria = 0 
for i in range (1, 101):
    sumatoria += i**2 * math.sin(i**2+3*math.pi)+i*math.cos(math.pi/i) 
    print("{:.5f}".format(sumatoria));
print("\nEl valor de la sumatoria es:","{:.5f}".format(sumatoria),"\n")