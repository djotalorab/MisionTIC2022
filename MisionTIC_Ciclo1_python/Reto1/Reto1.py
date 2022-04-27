# Te contrataron como ingeniero de software junior para desarrollar una aplicación, 
# para la empresa ServiPaquetes, que ayude con la gestión de los paquetes. 
# Específicamente para calcular el costo de los envíos de los paquetes. 
# Para ello, tú decides que harás la aplicación de forma progresiva, semana tras semana. 
# Es decir, el software que empieces a plantear desde esta semana, 
# igual será útil en la última semana. La empresa te indica que es fundamental que 
# sigas el orden en el que ellos te indican los datos, 
# puesto que el sistema de ellos los arroja en un orden específico.
#
# La empresa te dice que ellos calculan el costo de envío de un paquete, 
# multiplicando el volumen del paquete por $5.
#
#   volumen = alto x ancho x profundo
#
# Tu primera tarea será hacer que tu software calcule el volumen del paquete 
# y calcule el costo de envío.
#
# Lee detenidamente el planteamiento del reto, 
# cuando se te indique que hay que seguir un orden, es necesario que así sea. 
# Sigue atentamente los pasos de la solución del reto si tienes dificultades al resolverlo.
#
#
# PLANTEAMIENTO DEL RETO:
# Con respecto a la situación planteada, deberás crear 3 variables que leerán un número 
# FLOTANTE para el alto, ancho y profundo, EN ESE ORDEN. Luego, crea una variable, 
# con el nombre que desees, donde se guarde el cálculo del volumen del paquete, y otra donde 
# se guarde el cálculo del costo de envío. Finalmente, imprime el VOLUMEN del paquete y el 
# COSTO del envío, EN ESE ORDEN.
#
# IMPORTANTE: Cuando vayas a entregar el reto, quítale todos los textos decorativos o 
# informativos para el usuario. Solo debes dejar el código funcional. 
# Es decir, si imprimes cosas tipo “Ingrese …”, “El valor es …”, deberás de quitarlo. 
# Solo imprime lo que te indica el planteamiento del problema y en el orden en que se solicita.
#
#
# ACCIONES DE APRENDIZAJE:
#   a. Identifica las variables que se quieren definir.
#   b. Recordar de qué manera se pueden recolectar datos por entrada estándar para 
#      definir variables.
#   c. Recordar los operadores aritméticos para la definición de variables a partir 
#      de otras variables.
#
#
# SOLUCIÓN DEL RETO:
#   1. Debes recolectar los datos en el orden en el que se indica, para poder calcular 
#      el volumen.
#       a. Define una variable llamada alto y que esta lea, mediante entrada estándar, 
#          un número flotante.
#       b. Define una variable llamada ancho y que esta lea, mediante entrada estándar,
#          un número flotante.
#       c. Define una variable llamada profundo y que esta lea, mediante entrada estándar, 
#          un número flotante.
#
#   2. Debes de calcular el volumen, para esto define una variable llamada volumen y 
#      asígnale como valor alto*ancho*profundo.
#
#   3. Debes de calcular el costo de envío del paquete, para esto define una variable llamada 
#      costo y asígnale como valor volumen*5.
#
#   4. Imprime las respuestas:
#       a. Imprime la variable volumen
#       b. Imprime la variable costo

alto = float(input())
ancho = float(input())
profundo = float(input())
volumen = alto*ancho*profundo
costo = volumen*5
print(volumen)
print(costo)
