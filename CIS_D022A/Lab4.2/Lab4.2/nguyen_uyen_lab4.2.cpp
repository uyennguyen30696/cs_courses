//  Nguyen, Uyen
//  Lab 4.2
//  02/23/2022
//
//  Description: The switch statement and a loop

#include <iostream>
using namespace std;

int main() {
    char grade;
    char repeat = 'y';
    
    while (repeat == 'y' || repeat == 'Y') {
        cout << "What grade do you want to see? " << endl;
        cin >> grade;
        
        switch (grade) {
            case 'a':
            case 'A':
                cout << "Wow! Super!" << endl;
                break;
                
            case 'b':
            case 'B':
                cout << "Good job! Keep going!" << endl;
                break;
                
            case 'c':
            case 'C':
                cout << "Earning a C is satisfactory!" << endl;
                break;
                
            case 'd':
            case 'D':
                cout << "Just a bit more! You will do better next time." << endl;
                break;
            
            case 'f':
            case 'F':
                cout << "It's not the end of the world. True failure is only defined as quitting!" << endl;
                break;
                
            default:
                cout << "Invalid input" << endl;
                break;
        }
        
        cout << "Do you want to process another grade? (Y/N) " << endl;
        cin >> repeat;
    }
    
    return 0;
}
