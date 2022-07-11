/*
 * Planteamiento de la situación:
 * Dentro de las actividades de desarrollo de software de la compañía 
 * donde trabajas se utiliza tecnología Java, en uno de los proyectos 
 * surge la situación de agregar productos a un lote. 
 * El scrum master de tu equipo de desarrollo te asigna la incidencia 
 * para implementar una función que permita calcular el costo de 
 * almacenamiento dentro del módulo de productos.
 * 
 * Planteamiento del reto:
 * Generar una función llamada 
 * calcularCostoAlmacenamiento(boolean refigerado, float valorBase) 
 * que reciba dos parámetros, uno de tipo boolean que indica  si un 
 * medicamento es refrigerado o no refrigerado y otro de tipo float 
 * que indique el valorBaseDeAlmacenamiento del medicamento y retorne 
 * un valor float con el precio de almacenamiento teniendo en cuenta 
 * lo siguiente:
 * 
 *  Condiciones:
 *      - Si un medicamento  es refrigerado la variable booleana será true.
 *      - Si un medicamento es refrigerado su costo de almacenamiento tendrá 
 *          un 30% adicional al valor base, si no un costo adicional del 15%;
 *      - Tenga en cuenta el orden de los parámetros.
 * 
 *  Acciones de aprendizaje:
 *      - Analizar la situación problema
 *      - Seleccionar el tipo estructura/s de control que permitirán dar 
 *        solución a la situación planteada
 * 
 * */

package com.mycompany.reto1;

/**
 *
 * @author dajoo
 */
public class Reto1 {

    public static void main(String[] args) {
        System.out.println(calcularCostoAlmacenamiento(false, 10000));
    }

    public static float calcularCostoAlmacenamiento(boolean refrigerado, float valorBase){
        float precioAlmacenamiento = 0;
        if (refrigerado){
            precioAlmacenamiento = (float)(valorBase * 1.3);
        } else {
            precioAlmacenamiento = (float)(valorBase * 1.15);
        }
        return precioAlmacenamiento;
    }
}
