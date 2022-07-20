/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.clase7_1;

/**
 *
 * @author dajoo
 */
public class Profesor {
    
    public int cedula;    
    public String nombres;
    public String apellidos;
    public int edad;
    public String profesion;

    public Profesor(int cedula, String nombres, String apellidos, int edad, String profesion) {
        this.cedula = cedula;
        this.nombres = nombres;
        this.apellidos = apellidos;
        this.edad = edad;
        this.profesion = profesion;
    }

    public void mostrarProfesor(){
        System.out.println("\n[Profesor]:\nDocumento: "+cedula+"\nNombre: "+nombres+"\nApellido: "+apellidos+"\nEdad: "+edad+"\nProfesión: "+profesion+"\n");
    }  
    
    public void expertoPrincipiante(){
        if(edad>40){
            System.out.println("El profesor es Experto" + this.pension());
        } else {
            System.out.println("El profesor es principiante" + this.pension());
        }
    }

    public String pension() {
        String cadena = "";
        if (edad > 70){
            cadena = ". El profesor debería retirarse";
        } else {
            cadena = ". Aun es una edad laboral";
        }       
        return cadena; 
    }
}
