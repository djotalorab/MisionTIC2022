/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.clase3_1;

import java.util.Scanner;

/**
 *
 * @author dajoo
 */
public class Clase3_1 {

    public static void main(String[] args) {        
        Scanner digitado = new Scanner(System.in);

        System.out.println("Digite la cantidad de preguntas hechas al entrevistado: ");
        int preguntas = digitado.nextInt();
        System.out.println("Digite la cantidad de preguntas acertadas por el entrevistado: ");
        int respuestas = digitado.nextInt();

        float promedio = respuestas*100/preguntas;

        System.out.println("El porcentaje de aciertos es: "+ promedio + "%.");

        if (promedio >= 90){
            System.out.println("Nivel Máximo");
        } else if (promedio >= 75){
            System.out.println("Nivel medio");            
        } else if (promedio >= 50){
            System.out.println("Nivel Regular");
        } else {
            System.out.println("Fuera de nivel");
        }

        digitado.close();
    }
}
