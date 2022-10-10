# include <iostream>

using namespace std;

int main() {
//Lista a ordenar
int numeros[] = {3,9,2,8,6,7,1,5,4};
int aux; //Variable que ayuda a intercambiar numeros
int scan; //contador regresivo que ayuda a escanear lugares anteriores
cout<<"El Procedimiento es: "<<endl;
for(int i=0; i<9;i++){
    //scan se encarga de hacer la cuenta regresiva 
    scan = i;

    while(scan>0){

        if (numeros[scan]<numeros[scan-1]){
            //aqui se realiza un intercambio de valores
            aux = numeros[scan];
            numeros[scan] = numeros[scan-1];
            numeros[scan-1] = aux;
            
            for(int i=0;i<9;i++){
                if(i<8){
            cout<<numeros[i]<<", ";
                }else{
            cout<<numeros[i];
    }
    
}
cout<<endl;
        }
        scan--;

    }

//imprimir resultado


}
return 0;


}