/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.clase7_1;

import java.util.Scanner;

/**
 *
 * @author dajoo
 */
public class Clase7_1 {

    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        int cedula = teclado.nextInt();

        //Salto de linea antes de ingresar los string para limpiar buffer.
        teclado.nextLine();

        String nombre = teclado.nextLine();
        String apellido = teclado.nextLine();
        int edad = teclado.nextInt();
        teclado.nextLine();
        String profesion = teclado.nextLine();
        Profesor teacher = new Profesor(cedula,nombre,apellido,edad,profesion);
        teacher.mostrarProfesor();
        teacher.expertoPrincipiante();
        teclado.close();
    }
}
