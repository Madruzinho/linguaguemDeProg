#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int comparaInt(const void* a, const void* b) {
    int x = *(const int*)a;
    int y = *(const int*)b;
    return (x - y);
} 

int main() {
    srand(time(NULL));

    int numerosSorteados[200];
    for (int i = 0; i < 200; i++) {
        numerosSorteados[i] = rand() % 99 + 1;
    };

    cout << "Numeros gerados: ";
    for (int i = 0; i < 200; i++) {
        cout << numerosSorteados[i] << " ";
    };

    qsort(numerosSorteados, 200, sizeof(int), comparaInt);


    cout << "Numeros organizados com qsort: ";
     for (int i = 0; i < 200; i++) {
        cout << numerosSorteados[i] << " ";
    };


    return 0;
} 