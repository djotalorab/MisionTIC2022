/*
 * Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:
 * 
 *  - Si trabaja 40 horas o menos se le paga el 0.015 del SMLV por hora laborada.
 *  - Si trabaja más de 40 horas se le paga a 0.02 del SMLV por hora laborada.
 * 
 * Realice una función que se llame salario que reciba como parámetro la cantidad de horas 
 * del obrero y retorne un valor double con el salario devengado para dar solución al problema.
 * 
 * El SMLV es 1000000
 * */

package com.mycompany.cuiestionarioreto1;

import java.util.Scanner;

/**
 *
 * @author dajoo
 */
public class CuiestionarioReto1 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int horas = teclado.nextInt();        
        System.out.println(salario(horas));
        teclado.close();
    }

    public static double salario(int horas){
        int SMLV = 1000000;
        double pago = 0;
        double valorHora = 0;
        if(horas <= 40){
            valorHora = SMLV * 0.015;
        } else {
            valorHora = SMLV * 0.02;
        }
        pago = horas * valorHora;
        return pago;
    }
}
