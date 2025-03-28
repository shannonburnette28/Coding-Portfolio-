// Shannon Burnette - 2025 
// SCIS 123 
// Date: 03/5/2025
// Assignment: Lab  - Switcheroo
// Description: This program will determine if a highway number is valid and if it is a primary or auxiliary highway. It will also determine if the highway runs north/south or east/west.
#include <iostream>
using namespace std;

int main() {
    int highwayNum;
    bool NorthSouth = false;
    bool EastWest = false;
    bool isPrimary = false;
    bool isAuxiliary = false;

    // Prompt user to enter highway number
    cout << "Enter a highway number: ";
    cin >> highwayNum;

    // Check if the highway number is in the valid range
    if (highwayNum < 1 || highwayNum > 999) {
        cout << highwayNum << " is not a valid US interstate number" << endl;
    }
    else {
        // Determine whether the highway runs north/south or east/west
        if (highwayNum % 2 != 0) {
            NorthSouth = true;
            EastWest = false;
        } else {
            EastWest = true;
            NorthSouth = false;
        }

        // Check if the highway is a primary or auxiliary highway
        if (highwayNum >= 1 && highwayNum <= 99) {
            isPrimary = true;
            isAuxiliary = false;
        }
        else if (highwayNum >= 100 && highwayNum <= 999) {
            int lastTwoDigits = highwayNum % 100;
            if (lastTwoDigits != 0) {
                isAuxiliary = true;
                isPrimary = false;
            } else {
                cout << highwayNum << " is not a valid US interstate number" << endl;
                return 0; // End the program if invalid auxiliary highway
            }
        }

        // Output whether the highway is north/south or east/west
        if (NorthSouth) {
            cout << "The highway runs north/south" << endl;
        }
        if (EastWest) {
            cout << "The highway runs east/west" << endl;
        }

        // Output if the highway is primary or auxiliary
        if (isPrimary) {
            cout << "The highway is a primary highway" << endl;
        }
        if (isAuxiliary) {
            cout << "The highway is an auxiliary highway serving I-" << highwayNum % 100 << endl;
        }
    }

    return 0;
}
