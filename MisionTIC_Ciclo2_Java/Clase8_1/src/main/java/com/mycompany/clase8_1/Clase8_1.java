/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.clase8_1;

/**
 *
 * @author dajoo
 */
public class Clase8_1 {

    public static void main(String[] args) {
        Vehiculo carro = new Vehiculo("Juan Salvador Gaviota", "ABC123", "Pato", 2001, 2600, true);
        carro.mostrarVehiculo(); 

        Vehiculo chalupa = new Vehiculo("Gobierno", "NoTiene", "Gato", 2021, 4000, false);
        chalupa.mostrarVehiculo();
    }
}
