/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.clase7_2;

import java.util.Scanner;

/**
 *
 * @author dajoo
 */
public class Clase7_2 {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        String color = teclado.nextLine();
        double alto = teclado.nextDouble();
        double ancho = teclado.nextDouble();
        double largo = teclado.nextDouble();

        //Salto de linea antes de ingresar los string para limpiar buffer.
        teclado.nextLine();
        String material = teclado.nextLine();

        Mueble nuevoMueble = new Mueble(color, alto, ancho, largo, material);

        nuevoMueble.infoMueble();
        teclado.close();

    }
}
