/*
 * Un almacén ofrece descuentos a sus clientes de acuerdo al dia de la 
 * semana en que se realiza una determinada compra, si la compra se 
 * realiza lunes o jueves, se otorga descuento del 20%, martes o 
 * miercoles el 10%, si la compra se realiza cualquier otro día, no 
 * habrá descuento.
 * Realizar un programa que pida el día actual en letras y el valor de la compra; 
 * y muestre el descuento y el nuevo valor a pagar, de acuerdo a lo ingresado.
 * */

package com.mycompany.clase4_1;

import java.util.Scanner;

/**
 *
 * @author dajoo
 */
public class Clase4_1 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingrese el día de la semana: ");
        String dia = entrada.nextLine();
        dia = dia.toLowerCase();
        System.out.print("Ingrese el valor de la compra: $");
        float compra = entrada.nextFloat();
        float descuento = 0;
        float totalAPagar = 0;        
        if (dia.equals("lunes") | dia.equals("jueves")) {
            descuento = (float)(compra * 0.2);
            totalAPagar = (float)(compra - descuento);
            System.out.println("El descuento es: $" + descuento + "\nTotal a pagar: $" + totalAPagar);
        } else if (dia.equals("martes") | dia.equals("miercoles")) {
            descuento = (float)(compra * 0.1);
            totalAPagar = (float)(compra - descuento);
            System.out.println("El descuento es: $" + descuento + "\nTotal a pagar: $" + totalAPagar);
            } else {
                totalAPagar = (float)(compra - descuento);
                System.out.println("El descuento es: $" + descuento + "\nTotal a pagar: $" + totalAPagar);
                }
        
        entrada.close();
    }
}
