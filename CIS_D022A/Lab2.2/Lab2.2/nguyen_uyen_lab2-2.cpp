// Nguyen, Uyen
// Lab 2.1
// 01/21/2022
//
// Lab Description: Working with constants, variables and arithmetic operators
// Fill in the code so that the program will produce the following:
// The circumference of the circle is NN.NNNN. The area of the circle is NN.NNNN.

#include <iostream>
#include <string>
using namespace std;

const double PI = 3.14;
const double RADIUS = 8.3;
int main() {
    float area;  // declaration and definition of area
    float circumference; // declaration and definition of circumference
    
    circumference = 2 * PI * RADIUS; // computes circumference
    area = PI * RADIUS * RADIUS; // computes area
    
    cout << "circumference = " << circumference << endl;
    cout << "area = " << area << endl;

    return 0;
}
