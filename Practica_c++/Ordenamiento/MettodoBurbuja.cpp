# include<iostream>

using namespace std;

int main(){
//array con mis numeros a ordenar
    int numeros[] = {9,2,5,4,6,8,7,3,1};
    int aux; //Variable que funciona como pila para intercambiar el numero
    int count;//contador para el while, dice las veces que tuvo que ordenar un numero
    do{
        count = 0;// contador iniciado a 0, me dice si aun hay numeros por ordenar
        for (int i=0;i<9;i++){
            
            if (numeros[i]>numeros[i+1]){
                //se realiza un intercambio de numeros donde i se sustituye por el numero siguiente 
                aux = numeros[i];
                numeros[i] = numeros[i+1];
                numeros[i+1] = aux;
                count++;//marca que se realizo un cambio 
                };
            
        }
        
    }while(count!=0);
    cout <<"el resultado es "<<endl;
 /*   for (int i=0;0<10;i++){
        cout<<numeros[i]<<", ";
    }
*/
//imprimir resultado
    for (int i=0;i<9;i++){
        cout<<numeros[i]<<", ";
    }
    return 0;
}