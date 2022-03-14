// Nguyen, Uyen
// Lab 1.1
// 01/13/2022
//
// Lab Description: Compiling and Fixing a Program with a Syntax Error

#include <iostream>
using namespace std;

int main()
{
    int number;
    float total;
    
    cout << "Today is a great day for Lab";
    cout << endl << "Let's start off by typing a number of your choice" << endl;
    
    cin >> number;
    
    total = number * 2;
    
    cout << total << " is twice the number you typed" << endl;
    
    return 0;
}
