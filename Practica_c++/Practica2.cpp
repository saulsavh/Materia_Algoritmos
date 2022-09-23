
#include <iostream>

int main (){
    float n1,n2,suma=0, resta =0, multiplicacion=0;
    float division = 0;

    std :: cout << "digite un numero: "; std::cin>>n1;
    std :: cout <<"digite el segundo numero: "; std :: cin >> n2;

    suma = n1+n2;
    resta = n1-n2;
    multiplicacion = n1 *n2;
    division = n1/n2;

    std :: cout <<"La suma es: "<< suma <<" la resta es: "<<resta<<std::endl; 
    std :: cout <<"la multiplicacion es: "<< multiplicacion<<"  la division es: "<< division << std::endl;

}