/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.cuestionarioreto3;

/**
 *
 * @author dajoo
 */
public class CuestionarioReto3 {

    public static void main(String[] args) {
        Moto moto1 = new Moto(150, "XXSSDD");
        System.out.println(moto1.calcularImpuesto());
        
        Moto moto2 = new Moto(250, "aaeeuu");
        System.out.println(moto2.calcularImpuesto());
    }
}
