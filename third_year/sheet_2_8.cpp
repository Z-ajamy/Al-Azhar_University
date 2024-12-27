#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int x, n;
    cout << "Enter the number (x): ";
    cin >> x;
    cout << "Enter the number of digits (n): ";
    cin >> n;

    // Extract the first and last digits
    int last_digit = x % 10;
    int first_digit = x / static_cast<int>(pow(10, n - 1));

    double average;

    if (n % 2 == 1) { // Odd number of digits
        int middle_index = n / 2; // Middle index (zero-based)
        int middle_digit = (x / static_cast<int>(pow(10, middle_index))) % 10; // Extract middle digit
        average = (first_digit + middle_digit + last_digit) / 3.0;
    } else { // Even number of digits
        int first_middle_index = (n / 2) - 1; // First middle digit index
        int second_middle_index = n / 2;     // Second middle digit index

        int first_middle_digit = (x / static_cast<int>(pow(10, first_middle_index))) % 10; // First middle digit
        int second_middle_digit = (x / static_cast<int>(pow(10, second_middle_index))) % 10; // Second middle digit

        average = (first_digit + last_digit + first_middle_digit + second_middle_digit) / 4.0;
    }

    cout << "The average of the specified digits is: " << average << endl;

    return 0;
}
