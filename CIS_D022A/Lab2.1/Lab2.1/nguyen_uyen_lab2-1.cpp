// Nguyen, Uyen
// Lab 2.1
// 01/21/2022
//
// Lab Description: Working with the cout statement
// Fill in the code so that the program will do the following:
// Write your first and last name on one line.
// Write your address on the next line (recall the function of the endl statement).
// Write your city, state and zip on the next line.
// Write your telephone number on the next line.
// Remember that to output a literal, such as "Hello", you must use quotes.
// Compile and run the program.

#include <iostream>
#include <string>
using namespace std;

int main() {
    string firstName = "Uyen";
    string lastName = "Nguyen";
    string address = "21250 Stevens Creek Blvd";
    string city = "Cupertino";
    string state = "CA";
    string zip = "95014";

    cout << "Name: " << firstName << " " << lastName << endl;
    cout << "Address: " << address << endl;
    cout << city << ", " << state << ", " << zip << endl;

    return 0;
 }
