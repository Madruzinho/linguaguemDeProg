#include <iostream>
#include <map>

using namespace std;

int main() {
    map<string, int> notas;
    notas["Joao"] = 8;
    notas["Maria"] = 10;

    cout << "Nota de Maria: " << notas["Maria"] << endl;

    if (notas.find("Joao") != notas.end())
        cout << "Joao encontrado com nota " << notas["Joao"] << endl;

    if(notas.find("Guilherme") != notas.end())
        cout << "Guilherme encontrado com nota: " << notas["Guilherme"] << endl;
    else {
        cout << "Não encontrado Guilherme"; 
    }
    return 0;
}