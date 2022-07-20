/*
 * La empresa en la que trabajas ha regalado a sus empleados una tarjeta 
 * bono con $500.000 y como haces parte del equipo de sistemas de la empresa 
 * te piden realizar la implementación de un método/función para calcular un 
 * valor porcentual que se entregará de forma adicional a los empleados según 
 * su antigüedad en la empresa.
 * 
 * Debes utilizar la siguiente la siguiente plantilla:
 * 
 * public static double calcularPorcentajeBono(int anios,float bono) {
 *  double porcentaje;
 *  return porcentaje*bono;
 * }
 * 
 * Además los valores de descuento para el bono se aplicarán conforme a la siguiente tabla:
 * 
 *  Antigüedad en años                          Porcentaje aplicado
 *  mayor o igual a 10 años                         30%
 *  mayor o igual a 5 años pero menor a 10          20%
 *  mayor o igual a 3 años pero menor a 5           10%
 *  menor a 3 años                                  5%
 * 
 * a. Seleccionar el tipo estructura/s de control que permitirán dar solución a la situación planteada.
 * b. Verificar que la propuesta solución cumpla con lo solicitado al equipo de sistemas de la empresa.
 * c. Tener en cuenta el orden de los parámetros de la función.
 * 
 */

package com.mycompany.clase5_1;

/**
 *
 * @author dajoo
 */
public class Clase5_1 {

    public static void main(String[] args) {
        System.out.println(Clase5_1.calcularPorcentajeBono(20,500000));
        System.out.println(Clase5_1.calcularPorcentajeBono(7,500000));
        System.out.println(Clase5_1.calcularPorcentajeBono(4,500000));
        System.out.println(Clase5_1.calcularPorcentajeBono(2,500000));
    }


    public static double calcularPorcentajeBono(int anios,float bono) {
        
        double porcentaje=0;
        if(anios >= 10){
            porcentaje = 0.3;
        } else if (anios >= 5){
            porcentaje = 0.2;
        } else if (anios >= 3){
            porcentaje = 0.1;
        } else {
            porcentaje = 0.05;
        }
        return porcentaje*bono;
    }
}
