//Practica punteros con funciones

#include <iostream>
#include <stdio.h>
#include <string>
#include <cstdlib>

void sensado(float *a);

using namespace std;
int main ()
{
//practicando obtener el valor de saludo con la direccion
    string saludo = "Hola mundo";
    string *puntero = &saludo;
    float sensor;
    
    
    cout<<*puntero<<endl;
    cout<<puntero<<endl;
//practicando de obtener el valor de un sensor actualizando el valor directo en la direccion de memoria
    sensado(&sensor);
    cout << sensor<< endl;
    cout<<rand()%50;

    
    return 0;
}

void sensado(float *a){
    
    *a = 20 + (rand() % 50);
}
