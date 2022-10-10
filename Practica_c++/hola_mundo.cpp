#include<iostream> //Biblioteca donde se encuentra la función cout
using namespace std;  //uso del espacio de nombre std

int main(){           //inicio de la función main
	char nombre [] = "saul";
	int num = 2;
	int i;
	long z;
	float num2 = 5.9968;
	char letra;
	cout << "Hola Mundo!"<<endl;   //Imprimir en la consola
	printf("hola %s x%d, %f\n",nombre, num, num2);
	scanf("%d",&i);
	printf("%d\n",i);
	scanf("%lf",&z);
	printf("%f\n",z);
	scanf("%c",&letra);
	printf("%c\n",letra);
	return 0;                     //Al terminar, retornar 1.
}