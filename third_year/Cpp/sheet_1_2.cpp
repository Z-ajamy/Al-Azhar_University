/**
 * Write a program that asks for five test scores. The program should calculate
 * the average test score and display it
 */


#include<iostream>
using namespace std;

int main(void) {
    double first, second, third, fourth, fifth, average;
    cout << "Enter the first test score" << endl;
    cin >> first;
    cout << "Enter the second test score" << endl;
    cin >> second;
    cout << "Enter the third test score" << endl;
    cin >> third;
    cout << "Enter the fourth test score" << endl;
    cin >> fourth;
    cout << "Enter the fifth test score" << endl;
    cin >> fifth;

    average = first + second + third + fourth + fifth;
    average /= 5;
    cout << "the average test score is: " << average << endl;

    return 0;
}
