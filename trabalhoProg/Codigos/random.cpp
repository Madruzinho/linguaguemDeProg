#include <iostream>
#include <random>

using namespace std;

int main() {
    random_device rd;
    mt19937 gen(rd()); // motor de random
    uniform_int_distribution<> dist(1, 20);

    cout << "Dado jogado: " << dist(gen) << endl;
    cout << "Outro valor: " << dist(gen) << endl;
    return 0;
}