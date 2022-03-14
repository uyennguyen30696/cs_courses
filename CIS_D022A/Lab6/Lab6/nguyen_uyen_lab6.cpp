//  Nguyen, Uyen
//  Lab 5.1
//  03/06/2022
//
//  Description: The coin flip problem using functions

#include <iostream>
#include <cstdlib>   // Enables user of rand() function
using namespace std;


//  coinFlip function
void coinFlip(int& flip, int& headCount, int& tailCount) {
    // Randomly flip, head = 1, tail = 0
    flip = rand() % 2;
    
    // Calculate number of heads or tails
    if (flip == 1) {
        headCount++;
    }
    else if (flip == 0) {
        tailCount++;
    }
}

//  output function
void output(int& headCount, int& tailCount) {
    cout << "Wow! That’s " << headCount << " heads and ";
    cout << tailCount << " tails." << endl;
}


int main() {
    int numFlip = 0;
    int flip = 0;
    char repeat = 'y';
    
    //  Prompt the user for number of flips
    while (repeat == 'y' || repeat == 'Y') {
        int headCount = 0;
        int tailCount = 0;
        
        cout << "How many times do you want to flip the coin? ";
        cin >> numFlip;
        
        // Flip numFlip times
        for (int i = 0; i < numFlip; ++i) {
            coinFlip(flip, headCount, tailCount);
        }
        
        output(headCount, tailCount);

        cout << "Do you want to flip again? Y/N ";
        cin >> repeat;
        
        if (repeat == 'n' || repeat == 'N') {
            cout << "Thanks for flipping." << endl;
        }
    }

    return 0;
}
