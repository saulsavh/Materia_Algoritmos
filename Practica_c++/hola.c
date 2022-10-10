#include <stdlib.h>

int main(){

    int i;
    double num;
    char letra;

    printf("hola mundo\n");
    scanf("%d",&i);
    printf("tu numero es %d\n",i);
    printf("ingresa double ");
    scanf("%lf",&num);
    printf("tu numero es %f\n",num);
    printf("ingresa una letra \n");
    scanf("%s",letra);
    printf("tu letra es %s", letra);
    return 0;
}