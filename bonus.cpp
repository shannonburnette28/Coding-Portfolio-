// Shannon Burnette - SCIS 123 
// 03/07/2025 
// The purpose of this program is to create a menu for a restaurant that allows the user to order food and then checkout. 
//The program will display the menu and ask the user to enter their choice. 
//The user can order pizza, salad, or burger. 
//The program will display the price of the item and add it to the total price. 
//The user can continue to order items until they choose to checkout. 
//The program will display the order summary and the total price.
#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    char choice;
    double totalPrice = 0.0;
    int pizzaCount = 0, saladCount = 0, burgerCount = 0; // Count of each item ordered

    cout << "Welcome to the restaurant! Here is the menu:\n";
    cout << "P - Pizza ($6.99)\nS - Salad ($5.99)\nB - Burger ($7.99)\nC - Checkout\n";

    cout << "\nEnter your choice: ";
    cin >> ws >> choice; // `ws` ignores leading whitespace

    while (choice != 'C' && choice != 'c') { // Loop until the user chooses to checkout
        switch (choice) { // Determine the item ordered
            case 'P': case 'p':
                cout << "You ordered a pizza, which is $6.99\n";
                totalPrice += 6.99;
                pizzaCount++; // Increment the count of pizzas ordered
                break;
            case 'S': case 's':
                cout << "You ordered a salad, which is $5.99\n";
                totalPrice += 5.99;
                saladCount++;
                break;
            case 'B': case 'b':
                cout << "You ordered a burger, which is $7.99\n";
                totalPrice += 7.99;
                burgerCount++;
                break;
            default:
                cout << "Error - That is not a menu item\n";
        }

        cout << "\nEnter your choice: ";
        cin >> ws >> choice;
    }

    // Display summary of the order
    cout << "\nCheckout initiated...\n";
    cout << "\nOrder Summary:\n";
    if (pizzaCount > 0) cout << "Pizza(s): " << pizzaCount << " x $6.99\n"; // Display the count of each item ordered
    if (saladCount > 0) cout << "Salad(s): " << saladCount << " x $5.99\n";
    if (burgerCount > 0) cout << "Burger(s): " << burgerCount << " x $7.99\n";

    cout << fixed << setprecision(2); // Display the total price with 2 decimal places
    cout << "-------------------\n";
    cout << "Total Price: $" << totalPrice << endl;

    cout << "Thank you for your order!\n";

    return 0;
}