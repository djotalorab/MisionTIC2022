/*
 * Escribir un programa que solicite la carga de un valor 
 * positivo y nos muestre desde 1 hasta el valor ingresado 
 * de uno en uno.
 */

package com.mycompany.clase4_2ciclos;

import java.util.Scanner;

/**
 *
 * @author dajoo
 */
public class Clase4_2Ciclos {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Ingrese el número de iteraciones: ");
        int iteraciones = teclado.nextInt();

        System.out.println("\nCON FOR:\n");
        for (int i = 0; i < iteraciones; i++) {
            System.out.println("Iteración: " + (i+1));            
        }

        System.out.println("\nCON WHILE:\n");
        int i = 0;        
        while(i < iteraciones)
        {
            i++;
            System.out.println("Iteración: " + (i));
        }
        teclado.close();
    }
}
