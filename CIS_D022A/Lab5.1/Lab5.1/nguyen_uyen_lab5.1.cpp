//  Nguyen, Uyen
//  Lab 5.1
//  03/06/2022
//
//  Description: Working with arrays and vectors
//Welcome to the ranch!  It’s time to round up the cattle. The cowboys are busy every day
//rounding up strays and adding them in to the herd. We need to keep track of how many
//mavericks we get every day this week, and then total them up at the end of the week.
//FYI, a maverick is an unbranded cow, bull or calf. We get to brand them and keep them.

#include <iostream>
#include <string>
using namespace std;

const int numDays = 7;
// Function prototypes - print sunday to saturday
string dayOfWeek(int day);
int mostMavs(int allMavs[]);

int main() {
    int i;
    int mavsFound[numDays];
    int totalMavs = 0;
    
    for (i = 0; i < numDays; ++i) {
        cout << "How many mavericks on " << dayOfWeek(i) << "?" << endl;
        cin >> mavsFound[i];
        totalMavs += mavsFound[i];
    }
    cout << endl;
    for (i = 0; i < numDays; ++i) {
        cout << mavsFound[i] << endl;
    }
    cout << "Total mavericks found is " << totalMavs << endl;
    
    i = mostMavs(mavsFound);
    cout << dayOfWeek(i) << " had the most mavericks: " << mavsFound[i] << endl;
    
    return 0;
}

string dayOfWeek(int day) {
    if (day == 0) {
        return "Sunday";
    }
    else if (day == 1) {
        return "Monday";
    }
    else if (day == 2) {
        return "Tuesday";
    }
    else if (day == 3) {
        return "Wednesday";
    }
    else if (day == 4) {
        return "Thursday";
    }
    else if (day == 5) {
        return "Friday";
    }
    else if (day == 6) {
        return "Saturday";
    }
    
    return 0;
}

// Find the day of the largest mavericks found
int mostMavs(int allMavs[]) {
    int max = 0;
    int dayIndex = 0;
    int i;
    for (i = 0; i < numDays; ++i) {
        if (allMavs[i] > max) {
            dayIndex = i;
            max = allMavs[i];
        }
    }
    return dayIndex;
}
