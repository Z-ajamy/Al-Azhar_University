# include <iostream>
# include <cmath>
using namespace std;

int main(void) {
    double z, a, b, c;
    cout << "Enter the a value" << endl;
    cin >> a;
    cout << "Enter the b value" << endl;
    cin >> b;
    cout << "Enter the c value" << endl;
    cin >> c;

    z = (a) / (b - c);
    z = sqrt(z);

    cout << "z = " << z << endl;
    return 0;

}
