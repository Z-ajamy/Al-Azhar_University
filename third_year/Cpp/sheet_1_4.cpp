/**
 * Write a program that converts Celsius temperatures to Fahrenheit temperatures
 * the formula is f = (9/5)c + 32
 */

# include <iostream>
using namespace std;

int main(void) {
    double c, f;
    cout << "Enter the value of c" << endl;
    cin >> c;
    f = (9.0/5) * c + 32;
    cout << "the value of c is: " << f << endl;
    return 0;
}
