#include<iostream>

int numero;
using namespace std;
int main(){
    do
    {
        cout<<"Dame un numero entre 1 y 10"<<endl;
        cin>>numero;
    } while ((numero< 0) || (numero > 10));
    for(int i=1; i<10 ;i++){
        cout<<numero<<" * "<<i<<" = "<<numero*i<<endl;


    }

    return 0;
}