/**
 * Write a program in C++ to calculate the volume of a sphere using
 * the formula v = (4/3) Pi r^3
 */

# include <iostream>
# include <cmath>
using namespace std;

int main(void){
    double r, v, pi = 3.14;
    cout << "Enter the value of r " << endl;
    cin >> r;
    v = (4.0/3) * pi * pow(r, 3);

    cout << "the volume is: " << v << endl;
    return 0;
}
