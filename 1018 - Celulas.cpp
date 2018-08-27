#include <iostream>
using namespace std;
int main(){
int aux,cem,cinq,vinte,dez,cinco,dois,um;
cin >>aux;
if (aux >= 100){
    cem = aux/100;
    aux = aux-(100*cem);
}

if (aux >= 50){
    cinq = aux/50;
    aux = aux-(50*cinq);
}


cout << cem << "," << cinq << aux;
}
