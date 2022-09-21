#include<iostream> //Biblioteca donde se encuentra la función cout
string saludo;
using namespace std;  //uso del espacio de nombre std

int main(){           //inicio de la función main

	std::cout << "Hola Mundo!"<<endl;   //Imprimir en la consola
    saludo = cin<< "igrese nombre"<<endl; 
	return 0;                     //Al terminar, retornar 1.
}