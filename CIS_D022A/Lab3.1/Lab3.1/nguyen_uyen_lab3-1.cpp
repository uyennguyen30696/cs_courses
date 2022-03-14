//  Nguyen, Uyen
//  Lab 3.1
//  02/06/2022
//
//  Description: Random numbers, math library and mixed mode arithmetic

#include <iostream>
#include <iomanip>   // Enables use of fixed and setprecision() function
#include <cstdlib>   // Enables use of rand() function
#include <ctime>     // Enables use of time() function
#include <cmath>     // Enables use of sqrt() function

using namespace std;

int main() {
    int numRan1 = 0;
    int numRan2 = 0;
    double root1 = 0;
    double root2 = 0;
    double average = 0;
    char again = 'y';
    
    while (again == 'Y' || again == 'y') {
        srand((unsigned int) time(0));   // Unique seed
                                         // unsigned int is used to convert time from long to unsigned (avoid implicit warning)
                                         // Or: srand( static_cast<unsigned int>(time(NULL)));
        numRan1 = rand() % 20 + 1;
        numRan2 = rand() % 20 + 1;
        
        root1 = sqrt(numRan1);
        root2 = sqrt(numRan2);
        average = (numRan1 + numRan2) / 2;
        
        cout << "The two random numbers between 1 - 20 are " << numRan1;
        cout << " and " << numRan2 << endl;
        
        cout << "The square root of each number are " << fixed << setprecision(3) << root1;
        cout << " and " << fixed << setprecision(3) << root2 << endl;
        
        cout << "The average of the two numbers is " << fixed << setprecision(1) << average << endl;
        
        cout << "Do you want to repeat this program? Y/N " << endl;
        cin >> again;
    }
    
    return 0;
}
