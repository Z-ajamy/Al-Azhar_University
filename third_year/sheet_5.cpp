/**
 * Write a program in C++ to read two integers and swap them.
 */

# include <iostream>
using namespace std;

int main(void){
    int first, second, temp;
    cout << "Enter the first number" << endl;
    cin >> first;
    cout << "Enter the second number" << endl;
    cin >> second;

    temp = first;
    first = second;
    second = temp;

    cout << "The first number is: " << first << endl;
    cout << "The second number is: " << second << endl;

    return 0;
}
