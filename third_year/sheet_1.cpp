/**
 * Write a program to compute the perimeter of a triangle (p = a + b + c)
 */

#include<iostream>
using namespace std;

int main(void){
    int p, a, b, c;

    cout << "Enter the value of a" << endl;
    cin >> a;
    cout << "Enter the value of b" << endl;
    cin >> b;
    cout << "Enter the value of c" << endl;
    cin >> c;
    p = a + b + c;
    cout << "The value of the perimeter of a triangle (p = a + b + c) is: "  << p << endl;

    return 0;
}
