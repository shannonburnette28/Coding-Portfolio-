/*Prom Outfit Reccomendation System 
- Display a welcome message to greet the user
- Ask for user input on whether they'd like a tuxedo or dress 
    - store this response as outfitSelection 
- Ask for user input for their gender (Male or Female)
    - store this reponse as gender 
- Ask the user for input of their height on inches
    -store the value as height
- DETERMINE THE RECCOMMENDED OUTFIT SIZE: 
- Write a initial "if" statement for if the user chooses tuxedo: 
   -  nested if statement for height:
        - If height < 55 inches → Output "You need a short tuxedo"
        - Else if height is between 55 and 60 inches (inclusive) -> Output "You need a medium tuxedo"
        - Else (height > 60 inches) → Output "You need a tall tuxedo"
    - Close if statement for tuxedo 
- Write a initial "if" statement for if the user chooses dress: 
   -  nested if statement for height:
        - If height < 55 inches → Output "You need a petite dress"
        - Else if height is between 55 and 60 inches (inclusive) -> Output "You need a medium dress"
        - Else (height > 60 inches) → Output "You need a tall dress" 
    - Close if statement for dress
- End the program  */

//Shannon Burnette 
//SCIS 123 
//Prom Outfit Reccomendation System
// February 14, 2025
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
    string outfitChoice, gender;
    float height;

    // Display welcome message
    cout << "Welcome to the Prom Outfit Recommendation System!" << endl;

    // Get user input
    cout << "Would you like a tuxedo or dress? ";
    cin >> outfitChoice;
    cout << "Are you male or female? ";
    cin >> gender;
    cout << "Enter your height in inches: ";
    cin >> height;

    // Set precision for height output
    cout << fixed << setprecision(2);

    // Determine outfit recommendation
    if (outfitChoice == "tuxedo") {
        if (height < 55) {
            cout << "You need a short tuxedo." << endl;
        } else if (height <= 60) {
            cout << "You need a medium tuxedo." << endl;
        } else {
            cout << "You need a tall tuxedo." << endl;
        }
    } else if (outfitChoice == "dress") {
        if (height < 55) {
            cout << "You need a petite dress." << endl;
        } else if (height <= 60) {
            cout << "You need a medium dress." << endl;
        } else {
            cout << "You need a tall dress." << endl;
        }
    } else {
        cout << "Invalid choice. Please select either tuxedo or dress." << endl;
    }

    cout << "Thank you for using the system!" << endl;
    return 0;
}
