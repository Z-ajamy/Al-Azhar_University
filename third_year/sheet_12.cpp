/**
 * Write a program in C++ to read a float number and print the decimal part
 */

# include <iostream>
using namespace std;

int main(void){
    float num;
    cout << "Enter a float number" << endl;
    cin >> num;
    cout << "the decimal part is: " << (int)num << endl;
    return 0;
}
