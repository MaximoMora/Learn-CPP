#include <iostream>
#include <vector>


void jump_search(std::vector<int> list,int number) {
    
    int len = list.size();
    int jumps = std::sqrt(len);

    std::cout << len << " " << jumps << " " << number ;
}


int main() {

    std::vector<int> mivector = {1,2,3,4,5,6,7,8,9};
    int number =  4;
    jump_search(mivector,number);

}