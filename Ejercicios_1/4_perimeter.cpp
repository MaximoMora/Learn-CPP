#include <iostream>

using namespace std;

int main() {
    int side;

    cout << "dame el lado de un cuadrado: ";
    cin >> side;
    int perimeter = side * 4;
    int area = side * side;
    cout << "Perimetor: " << perimeter << " area: " << area;

}
