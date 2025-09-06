#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    vector<int> v = {5, 2, 9, 1, 7};
    sort(v.begin(), v.end());

    cout << "Ordenado: ";
    for (int n : v) cout << n << " ";
    cout << endl;

    if (find(v.begin(), v.end(), 9) != v.end())
        cout << "O numero 9 foi encontrado!" << endl;
    return 0;
}