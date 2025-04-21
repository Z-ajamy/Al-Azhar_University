/**
 * Write a C++ program to find the area of any triangle
 */

# include <iostream>
# include <cmath>
using namespace std;

int main(void) {
    double a, b, c, s, area;
    cout << "Enter the a value" << endl;
    cin >> a;
    cout << "Enter the b value" << endl;
    cin >> b;
    cout << "Enter the c value" << endl;
    cin >> c;

    s = (a + b +c) / 2;
    area = sqrt(s * (s - a) * (s - b) * (s - c));

    cout << "The area is: " << area << endl;

    return 0;

}
