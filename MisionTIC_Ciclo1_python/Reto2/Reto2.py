# Te contrataron como ingeniero de software junior para desarrollar una aplicación, 
# para la empresa ServiPaquetes, que ayude con la gestión de los paquetes. 
# Específicamente para calcular el costo de los envíos de los paquetes. 
# Para ello, tú decides que harás la aplicación de forma progresiva, semana tras semana. 
# Es decir, el software que empieces a plantear desde esta semana, 
# igual será útil en la última semana. La empresa te indica que es fundamental que 
# sigas el orden en el que ellos te indican los datos, 
# puesto que el sistema de ellos los arroja en un orden específico.
#
# La empresa te dice que ahora tienen una nueva política de costos porque ahora 
# deberán declarar IVA. Por esto, el costo de envío de un paquete, aunque seguirá siendo $5, 
# tiene estas nuevas consideraciones:
#
# Si la altura del paquete es mayor a 30 cm, al costo ya calculado se le suman $2000 adicionales. 
# También, si el costo es mayor a $10000, se le suma el valor del IVA (19%) como OTRO valor adicional.
# Por ejemplo, si un paquete mide 35 cm de alto, 10 cm de ancho y 5 cm de profundidad, 
# el costo sería $8750, pero como la altura es mayor a 30 cm, entonces se le aplica la tarifa adicional, 
# quedando el costo en $10750. Ahora, como el costo también es mayor a $10000, hay que sumarle el IVA 
# (19%) quedando un valor de $12792.5
#
# Tu tarea esta semana es hacer que el software de la semana pasada adopte esta nueva política de 
# costos de la empresa.

# Lee detenidamente el planteamiento del reto, cuando se te indique que hay que seguir un orden, 
# es necesario que así sea. Sigue atentamente los pasos de la solución del reto si 
# tienes dificultades al resolverlo.
#
# Planteamiento del reto
# Con respecto a la situación planteada, usa el código de la semana pasada y agrega los elementos 
# necesarios. Usa un condicional IF que haga que se agregue 2000 al costo si la altura es mayor a 
# 30 cm. Usa otro condicional IF que haga que se agregue el IVA del costo si el costo es mayor a 10000.
#
# Finalmente, imprime el VOLUMEN del paquete y el COSTO del envío, EN ESE ORDEN.
#
# IMPORTANTE: Cuando vayas a entregar el reto, quítale todos los textos decorativos o informativos 
# para el usuario. Solo debes dejar el código funcional. Es decir, si imprimes cosas tipo “Ingrese …”, 
# “El valor es …”, deberás de quitarlo. Solo imprime lo que te indica el planteamiento del problema 
# y en el orden en que se solicita.
#
# Acciones de aprendizaje
# 1. Identifica las variables que se quieren definir.
# 2. Recordar de qué manera se pueden recolectar datos por entrada estándar para definir variables.
# 3. Recordar los operadores aritméticos para la definición de variables a partir de otras variables.
# 4. Recordar el uso de los operadores de control IF.
#
# Solución del reto
# 1. Toma el código del reto anterior y elimina donde imprimes el volumen y el costo.
# 2. Agrega un condicional if que verifique si la variable alto es mayor que 30, en caso de cumplirse, 
#   debes sumarle al costo un valor de 2000.
# 3. Agrega un condicional if que verifique si la variable costo es mayor que 10000, 
#   en caso de cumplirse, debes sumarle al costo su IVA, ten en cuenta que el IVA es del 19%.
# 4. Imprime las respuestas:
#   a. Imprime la variable volumen
#   b. Imprime la variable costo

alto = float(input())
ancho = float(input())
profundo = float(input())
volumen = alto*ancho*profundo
costo = volumen*5
if alto > 30:
    costo += 2000
if costo > 10000:
    costo = costo+costo*0.19
print(volumen)
print(costo)