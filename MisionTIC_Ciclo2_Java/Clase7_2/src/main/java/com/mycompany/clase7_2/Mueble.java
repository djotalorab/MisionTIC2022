/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.clase7_2;

import java.lang.reflect.Constructor;

/**
 *
 * @author dajoo
 */
public class Mueble {

    private String color;
    private double alto;
    private double ancho;
    private double largo;
    private String material;

    public Mueble(String color, double alto, 
                        double ancho, double largo, 
                            String material) {
        this.color = color;
        this.alto = alto;
        this.ancho = ancho;
        this.largo = largo;
        this.material = material;
    }
    
    private double volumenMueble(){
        return  alto * ancho * largo;
    }
    public void infoMueble(){
        System.out.println("\nEl mueble es de color: "+color+
                            "\nAlto: "+alto+"\nAncho"+ancho+
                            "\nEsta hecho de: "+material+
                            "\nTiene una capacidad de: "+
                            volumenMueble()+"\n");
    }    
}
