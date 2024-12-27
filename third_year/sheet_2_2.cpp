# include <iostream>
# include <cmath>
using namespace std;

int main(void) {
    double z, a, b, c, d;
    cout << "Enter the a value" << endl;
    cin >> a;
    cout << "Enter the b value" << endl;
    cin >> b;
    cout << "Enter the c value" << endl;
    cin >> c;
    cout << "Enter the d value" << endl;
    cin >> d;

    z = pow(a,2);
    z += b;
    z = sqrt(z);
    z /= (c - pow(d, 2));

    cout << "z = " << z << endl;
    return 0;

}
