// Nguyen, Uyen
// Lab 1.2
// 01/13/2022
//
// Lab Description: This lab solves a logic error.
// Working with Logic Errors or “Help me!  My program gives bad answers!”

#include <iostream>
using namespace std;

int main()
{
    float firstNumber;
    float secondNumber;
    float tempNumber;
    
    // Prompt user to enter the first number.
    cout << "Enter the first number" << endl;
    cout << "Then hit enter" << endl;
    cin >> firstNumber;
    
    // Prompt user to enter the second number.
    cout << "Enter the second number" << endl;
    cout << "Then hit enter" << endl;
    cin >> secondNumber;
    
    // Echo print the input.
    cout << endl << "You input the numbers as " << firstNumber << " and " <<
    secondNumber << endl;
    
    // Now we will swap the values.
    tempNumber = firstNumber;
    firstNumber = secondNumber;
    secondNumber = tempNumber;
    
    //Output the values.
    cout << "After swapping, the values of the two numbers are " <<
    firstNumber << " and " << secondNumber << endl;
    return 0;
}
