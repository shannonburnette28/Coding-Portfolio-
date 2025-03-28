// Name: Shannon Burnette
/* Algorithm for String Processing Program

Purpose:
 - The program reads a string input from the user and processes it according to four specific conditions:

 - Display only the uppercase letters.

 - Display every second letter of the string.

 - Replace all vowels with underscores.

 - Identify and display the positions of all vowels in the string.

Step 1: Start
- Begin the program execution.

Step 2: Input Handling
- Prompt the user to enter a string.
- Read the entire line of text as a string input using getline() to ensure spaces are captured.

Step 3: Condition 1 - Display Uppercase Letters
- Display "Condition 1: " to indicate the output section.
- Initialize a loop to iterate through each character in the string:
- If the character is an uppercase letter (check using isupper()), print that character.
(End the loop.) 
- Move to the next line to separate this condition’s output from the next.

Step 4: Condition 2 - Display Every Second Letter
- Display "Condition 2: " to indicate the output section.
- Initialize a loop that starts at index 0 and increments by 2:
- Print the character at the current index.
(End the loop.) 
- Move to the next line.

Step 5: Condition 3 - Replace Vowels with Underscores
- Display "Condition 3: " to indicate the output section.
- Initialize a loop to iterate through each character in the string:
- If the character (converted to lowercase) is one of the following: 'a', 'e', 'i', 'o', 'u', print an underscore (_).
- Otherwise, print the character as it appears.
(End the loop.)  
- Move to the next line.

Step 6: Condition 4 - Display Vowel Positions
- Display "Condition 4: " to indicate the output section.
- Initialize a loop that iterates through each character in the string:
- If the character (converted to lowercase) is a vowel ('a', 'e', 'i', 'o', 'u'):
- Print the index of that character plus one (to represent a 1-based index).
(End the loop.) 
- Move to the next line.

Step 7: End Program
- Return 0 to indicate successful program termination.

Stop the program execution. */
// Date: 03/19/2025 

#include <iostream>
#include <cctype>
#include <string>
using namespace std;

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);

    // Condition 1: Only the uppercase letters in the string
    cout << "Condition 1: ";
    for (char c : input) {
        if (isupper(c)) {
            cout << c;
        }
    }
    cout << endl;

    // Condition 2: Every second letter of the string
    cout << "Condition 2: ";
    for (size_t i = 0; i < input.length(); i += 2) {
        cout << input[i];
    }
    cout << endl;

    // Condition 3: The string with all vowels replaced by underscores
    cout << "Condition 3: ";
    for (char c : input) {
        if (tolower(c) == 'a' || tolower(c) == 'e' || tolower(c) == 'i' || tolower(c) == 'o' || tolower(c) == 'u') {
            cout << '_';
        } else {
            cout << c;
        }
    }
    cout << endl;

    // Condition 4: The positions of all vowels in the string
    cout << "Condition 4: ";
    for (size_t i = 0; i < input.length(); ++i) {
        if (tolower(input[i]) == 'a' || tolower(input[i]) == 'e' || 
            tolower(input[i]) == 'i' || tolower(input[i]) == 'o' || tolower(input[i]) == 'u') {
            cout << i + 1 << " "; // Output 1-based index
        }
    }
    cout << endl;

    return 0;
}
