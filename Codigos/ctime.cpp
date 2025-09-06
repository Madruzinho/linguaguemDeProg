#include <iostream>
#include <ctime>

using namespace std;

int main() {
    time_t atual = time(NULL); 
    cout << "Segundos desde 1970: " << atual << endl;

    time_t agora = time(NULL); 
    tm* data = localtime(&agora); 

    char buffer[100];  
    strftime(buffer, 100, "%A, %d/%m/%Y %H:%M:%S", data);

    cout << "Data formatada: " << buffer << endl;

    return 0;
} 