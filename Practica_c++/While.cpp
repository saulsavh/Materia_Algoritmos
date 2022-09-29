// uso de while

#include <iostream>

int main(){
    int i = 0, a = 0, b = 0;
    int z = 0, x = 5, y = 1;
    
    while(i < 5){


        while (a < x){

            std :: cout <<" -";
            a++;

        }
        a=0;

        while (b < y){

            std :: cout <<" *";
            b++;
            }
        b=0;

        while (a < x){

            std :: cout <<" -";
            a++;
            }
        a=0;

    i++;
    x--;
    y+=2;

    std :: cout <<std :: endl;
    }
}
