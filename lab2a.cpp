/*Shannon K. Burnette 
February 05th 2025
Lab 2a: Math Functions & Output Formatting 

Prompt user to enter the principal balance in savings account 
Prompt user to enter the annual intrest rate 
Prompt user to eneter the number of times the intrest is compounded*/

//Format Text: 
 /*Intrest rate: 
 Times Compunded:  
 Principal: 
 Intrest: 
 Amount in Savings: */

 // Calculate Intrest : Principal * time * Intrest rate 
 // Calculate Total/Final Balance: Final Balance = Principal *(1 + Rate/T)^T

#include <iostream>
#include <cmath>
#include <iomanip>  // For formatting output

using namespace std;

int main() {
    float principalBal;
    float annIntRate;
    int timeComp;
    float interest;
    float finalBalance;

    // Prompt user input
    cout << "Please enter the original savings account balance: ";
    cin >> principalBal;

    cout << "Please enter the annual interest rate (as a percentage): ";
    cin >> annIntRate;
    annIntRate /= 100;  // Convert percentage to decimal

    cout << "Please enter the number of times interest is compounded (4 for quarterly, 12 for monthly): ";
    cin >> timeComp;

    // Calculate compound interest
    finalBalance = principalBal * pow(1 + (annIntRate / timeComp), timeComp);
    interest = finalBalance - principalBal;  // Interest earned

    // Format output
    cout << fixed << setprecision(2); // Set decimal places to 2

    cout << "\nInterest Rate: " << annIntRate * 100 << "%" << endl;
    cout << "Times Compounded: " << timeComp << endl;
    cout << "Principal: $" << principalBal << endl;
    cout << "Interest: $" << interest << endl;
    cout << "Amount in Savings: $" << finalBalance << endl;

    return 0;
}
