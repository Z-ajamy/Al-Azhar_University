/**
 * Write a C++ program that reads a number (x) and its number of digits (n) then compares
 * the first digit with the last digit and print the largest digit.
 * For example: if x=5672 and n=4 then the program will compare 5 and 2 and print 5
*/

# include <iostream>
# include <cmath>
using namespace std;

int main(){
    int num, len;
    cout << "Enter a number" << endl;
    cin >> num;
    cout << "Enter the length" << endl;
    cin >> len;

    int Fdig = num % 10;
    int Ldig = num / pow(10, (len - 1));

    if (Fdig > Ldig)
    {
        cout << Fdig << endl;
    }
    else
    {
        cout << Ldig << endl;
    }

    return 0;
}
