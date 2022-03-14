//  Nguyen, Uyen
//  Lab 3.2
//  02/06/2022
//
//  Description: Write a program that acts as a self-checkout register and lets the user buy 2 items

#include <iostream>
#include <iomanip>   // Enables use of fixed, setprecision(), and setw() function
#include <string>
using namespace std;

const double taxRate = 0.0925;
int main() {
    string item1, item2;
    int count1, count2;
    double price1, price2;
    double totalPrice1, totalPrice2;
    double totalTax1, totalTax2;
    double total;
    char yOrn;
    
//  Item 1, quantity and price
    cout << "Enter the name of item 1: ";
    getline(cin, item1);   // getline() to have cin item1 in multiple words with space in between without jumping to a new line
    cout << fixed << setprecision(2) << showpoint;
    cout << "Enter the number of " << item1 << " and the price of each: ";
    cin >> count1 >> price1;
    
//  Check for taxable
    cout << "Is (are) " << item1 << " food? Y/N ";
    totalPrice1 = price1 * count1;
    cin >> yOrn;
    if (yOrn == 'N' || yOrn == 'n') {
        totalTax1 = totalPrice1 * taxRate;
    }
    else {
        totalTax1 = 0.00;
    }
    
    cout << left << setw(20) << "-----------------------------" << endl;
    
//  Item 2, quantity and price
    cout << "Enter the name of item 2: ";
    cin.ignore();
    getline(cin, item2);
    cout << fixed << setprecision(2) << showpoint;
    cout << "Enter the number of " << item2 << " and the price of each: ";
    cin >> count2 >> price2;
    
//  Check for taxable
    cout << "Is (are) " << item2 << " food? Y/N ";
    totalPrice2 = price2 * count2;
    cin >> yOrn;
    if (yOrn == 'N' || yOrn == 'n') {
        totalTax2 = totalPrice2 * taxRate;
    }
    else {
        totalTax2 = 0.00;
    }
    
//  Total price of all items
    total = totalPrice1 + totalPrice2 + totalTax1 + totalTax2;
    
//  Format output into columns
    cout << setw(20) << left << "Item";
    cout << setw(16) << right << "Count";
    cout << setw(16) << right << "Price";
    cout << setw(16) << right << "Ext. Price";
    cout << setw(16) << right << "Tax" << endl;
    cout << left << setw(20) << "=====";
    cout << right << setw(16) << "=====" << setw(16) << "=====" << setw(16);
    cout << "=====" << setw(16) << "=====" << endl;
    
    cout << left << setw(20) << item1;
    cout << right << setw(16) << count1 << setw(16) << price1 << setw(16);
    cout << totalPrice1 << setw(16) << totalTax1 << endl;
    
    cout << left << setw(20) << item2;
    cout << right << setw(16) << count2 << setw(16) << price2 << setw(16);
    cout << totalPrice2 << setw(16) << totalTax2 << endl;
    
    cout << left << setw(20) << "Total tax";
    cout << right << setw(48) << totalTax1 + totalTax2 << endl;
    
    cout << left << setw(20) << "Total";
    cout << right << setw(48) << total << endl;

    return 0;
}
