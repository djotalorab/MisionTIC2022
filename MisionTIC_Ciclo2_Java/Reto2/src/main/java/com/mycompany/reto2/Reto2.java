/*
 * 
 * Planteamiento de la situación: 
 * Los pacientes de una EPS tienen distintos cobros de cuota moderadora y 
 * se requiere crear un programa para despachar el producto al paciente 
 * de acuerdo a su estado de cotización, si es cotizante debe pagar $3500 
 * y si no es cotizante, debe pagar $14000.
 * 
 * 
 * Planteamiento del reto:
 * Se requiere por parte de un desarrollador que se cree una clase,  la cual 
 * se debe llamar Producto, la clase debe estar diseñada de tal manera que, 
 * permita calcular su cuota moderadora y permita visualizar sus datos de 
 * entrada y los calculados.
 * 
 * 
 * Acciones de aprendizaje:
 *  - Interprete el diagrama de clase UML
 *  - Implementar una clase siguiendo un diseño establecido en un diagrama de clase 
 *  - Comprender la diferencia entre método constructor y otros métodos
 *  - Comprender la diferencia entre, atributo , parámetro y variable local 
 *  - Identificar los tipos de visibilidad de métodos y atributos
 *  - Realizar la implementación de un método conforme a los requerimientos del contexto
 * 
 * 
 * Solución del reto:
 *  - Interprete el diagrama de clase UML_Reto2.png
 *  - Implementar la clase Producto siguiendo un diseño establecido en el diagrama de clase
 *  - Agregar los atributos a la clase, según el tipo y visibilidad dados
 *  - Agregar el constructor
 *  - Implemente el método costo() que retorne el valor de de cuota moderadora según el contexto
 * 
 * */

package com.mycompany.reto2;

/**
 *
 * @author dajoo
 */
public class Reto2 {

    public static void main(String[] args) {
        Producto p1 = new Producto("Aspirina","abc","C","Tecnoquimicas",false);
        p1.info();
        System.out.println(p1.costo());
    }
}
