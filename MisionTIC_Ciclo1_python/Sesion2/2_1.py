# Importando libería Math
# Las funciones trigonométricas están en radianes en la librería Math.
# Los ángulos deben ser convertidos a Radianes. convierte con: math.radians(angulo)
# LA librería math no trabaja con numeros complejos. Debe importar cmath para complejos
# math.sqrt(9) ->->->->-> cmath.sqrt(-9)

import math

print(math.log(4))


# Ejercicio 1: 
# Un amigo quiere regalar a otro dos libros y los quiere legir entre los 15 que le gustan. 
# ¿De cuantas formas puede hacerlo?. Construya un Scrip que, al ejecutarlo, arroje el resultado.

# Función Comb...
Libros = 15
Regalos = 2
Comb = math.comb(Libros, Regalos)
print("\n l número de combinaciones es:",Comb)
#Impresión con el formato: (En caso de tener float, cammbiar a %f)
print("\nEl número de combinaciones de %d elementos entre %d elementos, es %d." %(Regalos, Libros, Comb))

#Calculando la combinatoria sin funcion comb, n!/(r!*(n-r)!)
CombF = (math.factorial(Libros)) / ((math.factorial(Regalos))*(math.factorial(Libros-Regalos)))
print("\nEl número de combinaciones de %d elementos entre %d elementos, es %d." %(Regalos, Libros, CombF))


# Ejercicio 2:
# Elabore un Scrip que muestre el factorial de un número, Considere que este número es de coma flotante

numero = 10.4
numeroApxA = math.ceil(numero)
numeroApxB = math.floor(numero)
factorial1 = math.factorial(numeroApxA)
factorial2 = math.factorial(numeroApxB)
print("\nEl factorial de %f redondeado hacia abajo es %d." %(numero,factorial2))
print("El factorial de %f redondeado hacia arriba es %d." %(numero,factorial1))


# Ejercicio 3:
# El radio de una circunferencia es de 5m. Escriba un código que, al ejecutarlo, determine el área del circulo. 
# Use la librería Math y defina la dimensión geométrica dada como la variable 'radio = "5"'. A=Pi*r**2

radio = "5"
radio =int(radio)
area = (math.pi)*(radio**2)
print("\nEl Area del circulo de radio %dm es %fm2." %(radio,area))


# Ejercicio 4:
# Construya un código que, dado un ángulo en angulos, calcule el valor de las seis variables trigonométricas principales.

angulo = 90
# Convierte el ángulo de grados a radianes.
angulorad = math.radians(angulo)
seno = math.sin(angulorad)
coseno = math.cos(angulorad)
tangente = math.tan(angulorad)
cotangente = 1/tangente
secante = 1/coseno
cosecante = 1/seno
# Convierte el ángulo de radianes a grados.
angulorad = math.degrees(angulorad)
print("\nEl seno de %d° es %f rad." %(angulo,seno))
print("El coseno de %d° es %f rad." %(angulo,coseno))
print("La tangente de %d° es %f rad." %(angulo,tangente))
print("La cotangente de %d° es %f rad." %(angulo,cotangente))
print("La secante de %d° es %f rad." %(angulo,secante))
print("La cosecate de %d° es %f rad." %(angulo,cosecante))


# Ejercicio 5:
# La siguiente ecuación permite calcular el factor de fricción (f) para un fluido a través de una tubería:
# 1/(raiz(f)) = -1,8log((6,9/Re)+(5x10^-6)).
# El parámetro Re depende del diámetro de la tubería (D), la velocidad del fluido (v), su densidad (p) y viscosidad (u):
# Re = (p*v*D)/u
#   p = 1000 
#   v = 8,5 
#   D = 0,2 
#   u = 1x10^-6
# Construya un scrip cuyo objetivo sea el cálculo del factor de fricción.

densidad = 1000
velocidad = 8.5
diametro = 0.2
viscosidad = 1e-6 # Uno por diez a la menos seis

Re = densidad * velocidad * diametro / viscosidad
x = -1.8*(math.log10(6.9/Re+5e-6))
friccion = (1/x)**2
print("\nEl factor de fricción es: %f." %(friccion))
print("El factor de fricción es: ", friccion)
print("El factor de fricción es: ", "{:.4f}".format(friccion)) #Impresión formateada en 4 digitos decimales.