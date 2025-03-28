/* Algorithm for Monthly Cell Phone Carrier Bill 
Step 1: Display Welcome Message 
- Print a message: "Welcome! This program calculates your monthly phone charge based on usage."

Step 2: Define Constants
- Set BASE_RATE = 29.95 (Fixed charge for up to 300 minutes)
- Set FREE_MINUTES = 300 (Minutes included in the base rate)
- Set EXTRA_RATE = 0.45 (Cost per additional minute if usage exceeds 300 minutes)
- Set TAX_RATE = 0.125 (Tax rate of 12.5%)

Step 3: Get User Input
- Ask the user: "Enter the total minutes used this month:"
- Store the input as an integer variable minutes_used

Step 4: Validate Input
- If minutes_used is less than 0:
- Print an error message: "Invalid input. Minutes cannot be negative."
- Stop the program.

Step 5: Check Usage and Compute Charges
- If minutes_used is less than or equal to FREE_MINUTES:
- Set total_charge = BASE_RATE
- Otherwise (if minutes_used is more than FREE_MINUTES):
- Compute extra_minutes = minutes_used - FREE_MINUTES
- Compute extra_charge = extra_minutes * EXTRA_RATE
- Compute total_charge = BASE_RATE + extra_charge

Step 6: Calculate Taxes
- Compute tax_amount = total_charge * TAX_RATE
- Compute final_charge = total_charge + tax_amount

Step 7: Display Output
- Print "Base charge: $" followed by BASE_RATE
- If there are extra minutes, print "Extra charge: $" followed by extra_charge
- Print "Tax amount: $" followed by tax_amount
- Print "Total amount due: $" followed by final_charge rounded to two decimal places

Step 8: End Program */

//Shannon K. Burnette 
// SCIS 123 
//February 21, 2025 

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    // Display welcome message
    cout << "Welcome! This program calculates your monthly phone charge based on usage." << endl;
    
    // Define constants
    const double BASE_RATE = 29.95;
    const int FREE_MINUTES = 300;
    const double EXTRA_RATE = 0.45;
    const double TAX_RATE = 0.125;
    
    // Get user input
    int minutes_used;
    cout << "Enter the total minutes used this month: ";
    cin >> minutes_used;
    
    // Validate input
    if (minutes_used < 0) {
        cout << "Invalid input. Minutes cannot be negative." << endl;
        return 1;
    }
    
    // Compute charges
    double total_charge = BASE_RATE;
    double extra_charge = 0.0;
    if (minutes_used > FREE_MINUTES) {
        int extra_minutes = minutes_used - FREE_MINUTES;
        extra_charge = extra_minutes * EXTRA_RATE;
        total_charge += extra_charge;
    }
    
    // Calculate tax and final charge
    double tax_amount = total_charge * TAX_RATE;
    double final_charge = total_charge + tax_amount;
    
    // Display output
    cout << fixed << setprecision(2);
    cout << "Base charge: $" << BASE_RATE << endl;
    if (extra_charge > 0) {
        cout << "Extra charge: $" << extra_charge << endl;
    }
    cout << "Tax amount: $" << tax_amount << endl;
    cout << "Total amount due: $" << final_charge << endl;
    
    return 0;
}
