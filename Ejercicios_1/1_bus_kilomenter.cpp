#include <iostream>

using namespace std;

int main() {
    int kilometer;
    int time;
    cout << "Distancia que viaja un bus en kilometros: ";
    cin >> kilometer;
    cout << "Tiempo que tiempo haciendo esta distancia: ";
    cin >> time;

    int speed = kilometer / time;

    cout << "Velocidad: " << speed;

} 
