/**
 * Write a program in C++ to read an integer and find the sum of the first and second digits of it
 */

# include <iostream>
using namespace std;

int main(void){
    int num, Fdig, Sdig, sum;
    cout << "Enter the number to get it's first digit" << endl;
    cin >> num;
    Fdig = num % 10;
    Sdig = num % 100;
    Sdig /= 10;
    sum = Fdig + Sdig;

    cout << "the sum of the first and second digits is: " << sum << endl;
    return 0;
}
