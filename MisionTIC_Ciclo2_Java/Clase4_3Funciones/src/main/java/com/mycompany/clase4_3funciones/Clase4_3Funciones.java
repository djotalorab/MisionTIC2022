/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.clase4_3funciones;

import java.util.Scanner;

/**
 *
 * @author dajoo
 */
public class Clase4_3Funciones {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.println("Ingrese dos numeros a sumar: ");
        int A = teclado.nextInt();
        int B = teclado.nextInt();
        int total = Clase4_3Funciones.sumarDosNumeros(A, B);
        System.out.println("El Resultado es: " + total);
        teclado.close();
    }

    public static int sumarDosNumeros(int A, int B) {
        int resultado;
        resultado = A + B;
        return resultado;        
    }

}
