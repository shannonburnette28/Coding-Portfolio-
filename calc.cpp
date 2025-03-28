/*  Program: Simple Calculator using Switch Statement
- Description: This program asks the user to choose an arithmetic operation - (addition, subtraction, multiplication, division), then takes two numbers as input and performs the chosen operation.
-  Algorithm:
    1. Display a menu asking the user to select an arithmetic operation (+, -, *, /).
    2. Read the user’s choice of operation.
    3. Prompt the user to enter two numbers.
    4. Read the two numbers entered by the user.
    5. Use a switch statement to perform the operation: The switch statement checks the user’s selected operation and executes the corresponding case.
       a. If the user selects '+', add the two numbers and display the result.
       b. If the user selects '-', subtract the second number from the first and display the result.
       c. If the user selects '*', multiply the two numbers and display the result.
       d. If the user selects '/', check if the second number is zero:
         i. If not, divide the first number by the second and display the result.
          ii. If zero, display an error message indicating division by zero is not allowed.
       e. If the user enters an invalid operation, the default case executes, displaying an error message.
    6. The switch statement is used because it allows efficient selection of operations based on a single user input,
       making the code more readable and easier to maintain compared to multiple if-else statements.
    7. End the program.
*/
//Shannon K. Burnette 
//SCIS 123 
//Date: 10/10/2021

#include <iostream>
using namespace std;

int main() {
    char operation;
    double num1, num2, result;
    
    // Display menu
    cout << "Simple Calculator" << endl;
    cout << "Select an operation (+, -, *, /): ";
    cin >> operation;
    
    // Get user input for numbers
    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter second number: ";
    cin >> num2;
    
    // Perform operation using switch statement
    switch(operation) {
        case '+':
            result = num1 + num2;
            cout << "Result: " << num1 << " + " << num2 << " = " << result << endl;
            break;
        case '-':
            result = num1 - num2;
            cout << "Result: " << num1 << " - " << num2 << " = " << result << endl;
            break;
        case '*':
            result = num1 * num2;
            cout << "Result: " << num1 << " * " << num2 << " = " << result << endl;
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
                cout << "Result: " << num1 << " / " << num2 << " = " << result << endl;
            } else {
                cout << "Error: Division by zero is not allowed." << endl;
            }
            break;
        default:
            cout << "Invalid operation! Please select +, -, *, or /." << endl;
    }
    
    return 0;
}
