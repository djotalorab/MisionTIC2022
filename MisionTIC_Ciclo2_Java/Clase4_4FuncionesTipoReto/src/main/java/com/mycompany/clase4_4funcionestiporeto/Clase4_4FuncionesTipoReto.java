/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.clase4_4funcionestiporeto;

/**
 *
 * @author dajoo
 */
public class Clase4_4FuncionesTipoReto {

    public static void main(String[] args) {
        double valorFinal = Clase4_4FuncionesTipoReto.rango(3, 40);
        System.out.println(valorFinal);
    }
    public static double rango(int capacidad, float milesPerGallon){
        double productoFinal;
        double producto = (capacidad * milesPerGallon);
        if (capacidad <= 4){
            productoFinal = producto * 1.15;
        } else if (capacidad <= 9){
            productoFinal = producto * 1.25;
        } else {
            productoFinal = producto * 1.33;
        }
        return productoFinal;
    }
}
