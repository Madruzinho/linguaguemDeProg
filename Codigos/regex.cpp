#include <iostream>
#include <regex>

using namespace std;

int main() {
    string email = "teste@cefetmg.br";
    regex padraoemail(".+@.+\\..+"); // verifica se tem algo antes e depois do @, e se tem . + alguma coisa

    if (regex_match(email, padraoemail))
        cout << email << " e valido\n";

    string texto = "O numero e 12345.";
    regex numeros("[0-9]+");
    cout << "Substituido: " << regex_replace(texto, numeros, "xxxxx") << endl;
    return 0;
}
