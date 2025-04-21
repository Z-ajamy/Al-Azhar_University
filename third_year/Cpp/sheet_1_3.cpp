/**
 * Write a program that asks the user for the number of males and the number of
 * females registered in a class. The program should display the percentage of
 * males and females in the class
 */


# include <iostream>
using namespace std;

int main(void) {
    double male, female, sum, percentage_of_male;

    cout << "Enter the number of males" << endl;
    cin >> male;
    cout << "Enter the number of females" << endl;
    cin >> female;

    sum = male + female;
    percentage_of_male = (male * 100/ sum) ;

    cout << "percentage of males is: " << percentage_of_male << "%" << endl;
    cout << "percentage of females is: " << 100 - percentage_of_male << "%" << endl;


    return 0;
}
