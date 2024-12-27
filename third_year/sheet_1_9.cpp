/**
 * Write a program in C++ to read an integer and find the first digit of it
 */

# include <iostream>
using namespace std;
int main(void){
    int num;
    cout << "Enter the number to get it's first digit" << endl;
    cin >> num;
    cout << "the first digit of it is: " << num % 10 << endl;

    return 0;
}
