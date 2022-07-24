/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.cuestionarioreto3;

/**
 *
 * @author dajoo
 */
public class Moto extends Vehiculo {
    
    private int cilindraje;

    public Moto(int cilindraje, String placa) {
        super(placa);
        this.cilindraje = cilindraje;
    }

    public int calcularImpuesto(){
        int retorno = 45000;
        if(this.cilindraje > 150){
            retorno = 90000;
        }
        return retorno;
    }

}
