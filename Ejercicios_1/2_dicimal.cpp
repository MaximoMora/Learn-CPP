#include <iostream>
#include <math.h>

using namespace std;

int main() {
    float decimal;
    cout << "give a decimal: ";
    cin >> decimal;
    float poynomial = 3*pow(decimal,4)-10*pow(decimal,3)+21;
    cout << "polinomio evaluado: " << poynomial;

}