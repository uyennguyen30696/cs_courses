//  Nguyen, Uyen
//  Lab 4.1
//  02/23/2022
//
//  Description: Write a program demonstrating nested loops

#include <iostream>
using namespace std;

int main() {
    int outer;
    int inner;
    int i;
    int j;

    cout << "How many times do you want the outer loop to run?" << endl;
    cin >> outer;
    cout << "How many times do you want the inner loop to run?" << endl;
    cin >> inner;
    
    int totalIterations = outer * inner;

    for (i = 1; i <= outer; ++i) {
        cout << "Outer loop iteration: " << i << endl;
        cout << endl;
        for (j = 1; j <= inner; ++j) {
            cout << "Inner loop iteration: " << j << endl;
        }
        cout << endl;
    }
    
    cout << "Total iterations of the inner loop is " << totalIterations << endl;
    
    return 0;
}
