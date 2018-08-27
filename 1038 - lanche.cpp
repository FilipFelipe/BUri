#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
float valor[6] ={0,4,4.5,5,2,1.5};
float resul;
int aux,op;
cin >> aux;
cin >> op;
resul = valor[aux]*op;
printf("Total: R$ %.2f\n",resul);
}
