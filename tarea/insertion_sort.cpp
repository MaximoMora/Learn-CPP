#include <iostream>
#include <vector>

int insertion_sort(std::vector<int> list) {
    int len = list.size();
    for (int i = 0; i < len; i++)
    {
        int min = list[i];
        int min_index = i;
        for (int j = i; j < len; j++)
        {
            if (list[j] < min)
            {
                min = list[j];
                min_index = j;                   
            }
        }
        int aux = list[i];
        list[i] = min;
        list[min_index] = aux;
    }

    for (int k = 0; k < len; k++)
    {
        std::cout << list[k];
    }
      
}
int main() {

    std::vector<int> lista= {4,3,2,7,4,6,1};
    insertion_sort(lista);


    return 0;
}