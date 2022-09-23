

#include <iostream>

int main(){
    char letra;

    std :: cout<<"Quiere continuar? S/n"<<std::endl;
    std :: cin >> letra;

    if (letra == 'S' or letra == 's'){
        std :: cout <<"puede continuar";
    }
    else if (letra == 'N' or letra == 'n'){
        std :: cout << "Entendido, Saliendo...";
    }
    else {
        std :: cout <<"Valor no admitido ... ";
    }
    
    return 0;

}