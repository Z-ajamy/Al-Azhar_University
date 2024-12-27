/**
 * Write a program in C++ to read an integer and remove the first digit of it
 */

# include <iostream>
using namespace std;

int main(void){
    int num;
    cout << "Enter the number to remove the first digit" << endl;
    cin >> num;
    cout << "The number without it's first digit: " << num / 10 << endl;
    return 0;
}
