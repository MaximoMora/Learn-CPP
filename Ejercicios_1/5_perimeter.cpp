#include <iostream>

using namespace std;

int main() {
    int width;
    int height;
    cout << "dame el ancho de un rectangulo: ";
    cin >> width;
    cout << "dame el altura de un rectangulo: ";
    cin >> height;
    int perimeter = (width * 2) + (height * 2);
    int area = width * height;
    cout << "Perimetor: " << perimeter << " area: " << area;

}
