#include <iostream>
#include <queue>

using namespace std;

int main() {

    queue<string> fila;
    fila.push("primeiro");
    fila.push("segundo");

    cout << "Frente da fila: " << fila.front() << endl;
    fila.pop();
    cout << "Agora na frente: " << fila.front() << endl;
    return 0;
}