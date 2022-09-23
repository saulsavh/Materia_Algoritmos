

#include <iostream>

int main(){
    char opciones;
    std :: cout <<"Seleccione el valor a, b o c"<<std::endl;
    std :: cin >> opciones;

    switch (opciones){
        case 'a':
            std :: cout <<"opcion A"<<std::endl; break;
        case 'b':
            std :: cout <<"opcion B"<<std::endl; break;
        case 'c':
            std :: cout <<"opcion C"<<std::endl; break;
        default:
            std :: cout <<"opcion no Valida"<<std::endl; break;
    }


    return 0;
}