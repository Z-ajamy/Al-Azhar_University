/**
 * Write a program in C++ to read two angles and find the third angle of a triangle
 */

# include <iostream>
using namespace std;

int main(void){
    double angle1, angle2, angle3;
    cout << "Enter the first angle" << endl;
    cin >> angle1;
    cout << "Enter the second angle" << endl;
    cin >> angle2;
    angle3 = 180 - (angle1 + angle2);

    cout << "the third angle is: " << angle3 << endl;

    return 0;
}
