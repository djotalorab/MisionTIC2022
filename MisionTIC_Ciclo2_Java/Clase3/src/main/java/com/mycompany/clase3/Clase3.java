/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.clase3;

import java.util.Scanner;

import javax.swing.JOptionPane;

/**
 *
 * @author dajoo
 */
public class Clase3 {
    public static void main(String[] args) {
        Scanner digitado = new Scanner(System.in);
        System.out.println("Ingrese el salario del empleado: ");
        float sueldo = digitado.nextFloat();
        System.out.println("Ingrese los años de antiguedad del empleado: ");
        int antiguedad = digitado.nextInt();
        if (sueldo < 1000000){
            if (antiguedad >= 10){
                sueldo = (float) (sueldo * 1.2);
                System.out.println("El nuevo salario del empleado es: $" + sueldo);
            } else {
                sueldo = (float) (sueldo * 1.05);
                System.out.println("El nuevo salario del empleado es: $" + sueldo); 
            }
        } else {
            System.out.println("El empleado gana: $" + sueldo + ", no se puede aplicar aumento.");
        }
        digitado.close();
    }
}
