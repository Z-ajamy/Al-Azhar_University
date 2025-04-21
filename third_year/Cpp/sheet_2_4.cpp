/**
 * Write a C++ program that reads the user’s weight and height then calculates his/her Body
 * Mass Index (BMI) 
 */

# include <iostream>
# include <cmath>
using namespace std;

int main(){
    double height, weight, BMI;
    cout << "Enter your height (in cm)" << endl;
    cin >> height;
    cout << "Enter your weight (in kg)" << endl;
    cin >> weight;

    height = height / 100;

    BMI  = weight / pow(height, 2);

    if (BMI <= 18.5)
    {
        cout << "Underweight" << endl;
    }
    else if (BMI <= 24.9)
    {
        cout << "Normal weight" << endl;
    }
    else if (BMI <= 29.9)
    {
        cout << "Pre-obesity" << endl;
    }
    else if (BMI <= 34.9)
    {
        cout << "Obesity class I" << endl;
    }
    else if (BMI <= 39.9)
    {
        cout << "Obesity class II" << endl;
    }
    else if (BMI > 39.9)
    {
        cout << "Obesity class III" << endl;
    }
    
    return 0;
}
