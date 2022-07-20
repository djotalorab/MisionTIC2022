/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.clase8_1;

/**
 *
 * @author dajoo
 */
public class Vehiculo {
    
    private String propietario, placa, marca;
    private int modelo, cilindraje;
    private boolean tipoVehiculo;
    private float impuestoVehicular;

    public Vehiculo(String propietario, String placa, String marca, int modelo, int cilindraje, boolean tipoVehiculo) {
        this.propietario = propietario;
        this.placa = placa;
        this.marca = marca;
        this.modelo = modelo;
        this.cilindraje = cilindraje;
        this.tipoVehiculo = tipoVehiculo;
        this.impuestoVehicular = calcularImpuesto();
    }

    public void mostrarVehiculo(){
        System.out.println("\nPropietario: "+propietario+
                            "\nPlaca: "+placa+
                            "\nMarca: "+marca+
                            "\nModelo: "+modelo+
                            "\nCilindraje: "+cilindraje+
                            "\nImpuesto: "+impuestoVehicular+"\n");
    }

    private float calcularImpuesto(){
        float impuesto = 0;
        double t = 0.42;
        double fa = 0.2;

        if (this.cilindraje <= 1700){t = 0.0;}
        else if (this.cilindraje <= 2000){t = 0.08;}
        else if (this.cilindraje <= 2500){t = 0.09;}
        else if (this.cilindraje <= 3000){t = 0.14;}
        else if (this.cilindraje <= 3500){t = 0.18;}
        else if (this.cilindraje <= 4000){t = 0.24;}
        
        int antiguedad = 2022 - this.modelo;
        if(antiguedad < 5){fa = 0.0;}
        else if(antiguedad <= 10){fa = 0.05;}
        else if(antiguedad <= 15){fa = 0.10;}
        else if(antiguedad <= 20){fa = 0.15;}

        impuesto = (float)(((cilindraje-1500)*t)*(1+fa));
        if(this.tipoVehiculo){
            impuesto = (impuesto*1854);
        } else {
            impuesto = (impuesto*1412);
        }
        return impuesto;
    }
}
