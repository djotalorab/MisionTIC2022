/*
 * Planteamiento del problema
 * La farmacia misión tic tiene 4 almacenes ubicados así: 
 * oriente, occidente, norte y sur, cada almacén contiene un 
 * lote de productos que se clasifican en productos 
 * refrigerados y no refrigerados. Se requiere llevar mayor 
 * control de los datos que allí disponen, el líder de 
 * desarrollo decide contratar a su grupo de trabajo y le 
 * indica lo siguiente:
 * 
 * De cada producto se tienen los siguientes datos:
 * 
 * De cada producto se tienen los siguientes datos.
 *  - Nombre, de tipo String.
 *  - ID: código del producto, de tipo String.
 *  - temperatura (temperatura a la que se almacena), de 
      tipo double.
 *  - Valor base de almacenamiento, double
 * 
 * A continuación, se presenta un ejemplo de productos 
 * registrados:
 * 
 *  Tabla 1:
 *  NOMBRE                      ID.     °C máximo   Valor base
 *  Suero                       14589       25 °C      $1.500
 *  Antibiótico en pastilla     57896       30 °C      $1.000
 *  Vacunas                     32658       10 °C      $2.000
 * 
 * 
 *  Tabla 2: 
 *  Tipo de refrigeración   Valor por unidad    Rango temperatura
 *  Refrigerado             120% del valor base     0 a 20 °C
 *  No refrigerado          110% del valor base     21 °C en adelante
 * 
 * 
 * Actualmente se cuenta con el siguiente diagrama de clases: DIAGRAMA EN CARPETA
 * 
 * Planteamiento del reto:
 * Dada la situación planteada, el administrador de la 
 * farmacia te explica que ya tienen implementadas las clases 
 * Farmacia, Almacén, Lote, y ProductoRefrigerado. Por 
 * cambios en la compañía, se hace necesario calcular el 
 * costo de almacenamiento de los productos no refrigerados, 
 * y es por este motivo que te han contratado para implementar 
 * la clase ProductoNoRefrigerado, teniendo en cuenta que el 
 * costo de almacenamiento está basado en la información de 
 * la tabla 2
 * 
 * Acciones de aprendizaje:
 * -Analizar e identificar las variables que considere 
 *  necesarias para la correcta ejecución del programa.
 * -Interpretar el diagrama de clase.
 * -Realizar las implementaciones adicionales que requiere el 
 *  problema.
 * -Comprender el encadenamiento de constructores.
 * 
 * Solución del reto:
 * Escriba el código de la clase ProductoNoRefrigerado que 
 * cumpla con los siguientes requisitos:
 * -Debe heredar de la clase Producto
 * -Realizar la implementación del método 
 *  calcularCostoDeAlmacenamiento() según los requerimientos 
 *  del contexto
 * 
 * Por ejemplo:
 * 
 *  Test:
 *  ProductoNoRefrigerado p= new ProductoNoRefrigerado();
 *  p.setValorBase(1000);
 *  System.out.println(p.calcularCostoDeAlmacenamiento());
 * 
 *  Resultado:
 *  1100.0
 * 
 */

package com.mycompany.reto3;

/**
 *
 * @author dajoo
 */
public class Reto3 {

    public static void main(String[] args) {
        ProductoNoRefrigerado p= new ProductoNoRefrigerado();
        p.setValorBase(1000);
        System.out.println(p.calcularCostoDeAlmacenamiento());
    }
}
