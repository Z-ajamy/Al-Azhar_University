/**
 * Write a program that reads a character and tests whether it is a vowel or not.
 */

#include <iostream>
using namespace std;

int main() {
    char ch;
    cout << "Enter a character: ";
    cin >> ch;

    // Convert to lowercase for case-insensitive comparison
    ch = tolower(ch);

    // Check if the character is a vowel
    if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
        cout << ch << " is a vowel." << endl;
    } else {
        cout << ch << " is not a vowel." << endl;
    }

    return 0;
}
