// Program: Multiplication table using while, for, and do-while loops
// Purpose: To display the multiplication table of a number entered by the user
// Shannon Burnette 
// 03/23/2025
#include <iostream>
using namespace std;

int main() {
    int num;

    cout << "Enter a number: ";
    cin >> num;

    cout << "\nMultiplication table using while loop:\n";
    int i = 0;
    while (i <= 10) {
        cout << num << " x " << i << " = " << num * i << endl;
        i++;
    }

    cout << "\nMultiplication table using for loop:\n";
    for (int j = 0; j <= 10; j++) {
        cout << num << " x " << j << " = " << num * j << endl;
    }

    cout << "\nMultiplication table using do-while loop:\n";
    int k = 0;
    do {
        cout << num << " x " << k << " = " << num * k << endl;
        k++;
    } while (k <= 10);

    return 0;
}