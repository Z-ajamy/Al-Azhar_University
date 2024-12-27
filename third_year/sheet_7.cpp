/**
 * Write a program in C++ to calculate the volume of a cube using the formula V = L^3
 */

# include <iostream>
# include <cmath>
using namespace std;

int main(void) {
    double V, L;
    cout << "Enter the L" << endl;
    cin >> L;
    V = pow(L, 3);

    cout << "The volume of a cube is: " << V << endl;

    return 0;
}
