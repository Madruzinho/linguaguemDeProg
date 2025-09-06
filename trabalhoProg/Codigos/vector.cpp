#include <iostream>
#include <vector>

using namespace std;

int main() {
    
    vector<int> v;
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);

    cout << "Tamanho do vetor: " << v.size() << endl;
    cout << "Primeiro elemento: " << v.at(0) << endl;
    return 0;
}