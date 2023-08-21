#include <iostream>
#include <vector>

void bubble(std::vector<int> list) {
    int len = list.size();

    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len -1; j++)
        {
            if (list[j] > list[j+1]) {
                int aux = list[j];
                list[j] = list[j+1];
                list[j+1] = aux;
            }
        } 
    }

    for (int k = 0; k < len; k++)
    {
        std::cout << list[k];
    }
    

}

int main() {
    std::vector<int> hola = {8,2,1,4,5,6};


    return 0;

}