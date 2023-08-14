#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream text("people.csv");
    cout << "hola " << text;
}