/* Step 1: Display Welcome Message:
Print a message informing the user about the program’s purpose.
    -Example output: "Welcome! This program calculates change using the fewest number of coins."

Step 2: Take User Input:
Prompt the user to enter an integer representing the total change amount in cents.
    - Store this input as an integer variable named total_change.
    - Ensure proper data type handling to prevent errors (use integer conversion if needed).
        *Example input: total_change = int(input("Enter the total change amount (in cents): "))

Step 3: Validate Input:
If total_change is less than or equal to 0, print "No change" and terminate the program.
    - Example condition: if total_change <= 0: print("No change")
    - Exit the program using return or exit() if the condition is met.

Step 4: Define Coin Values and Initialize Output List:
Declare constant integer variables for coin values:
    DOLLAR = 100
    QUARTER = 25
    DIME = 10
    NICKEL = 5
    PENNY = 1
    - Create an empty list named output_list to store coin descriptions dynamically.
        * Example: output_list = []

Step 5: Calculate Coins Needed:
Initialize variables for each coin type:
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    - Compute the number of coins needed for each denomination based on the total change amount.
    - Update the total_change value after calculating each coin type.

Step 5.1: Compute Dollars:
If total_change is greater than or equal to DOLLAR, compute the number of dollars:

    dollars = total_change // DOLLAR

Subtract the corresponding value from total_change:

    total_change -= dollars * DOLLAR

Append the correct dollar description to output_list:

    If dollars == 1, append "1 Dollar"

Else, append "X Dollars" (where X is the computed value)

Step 5.2: Compute Quarters
If total_change is greater than or equal to QUARTER, compute the number of quarters:

    quarters = total_change // QUARTER

Subtract the corresponding value from total_change:

    total_change -= quarters * QUARTER

Append the correct quarter description to output_list:

    If quarters == 1, append "1 Quarter"

Else, append "X Quarters"

Step 5.3: Compute Dimes

If total_change is greater than or equal to DIME, compute the number of dimes:

    dimes = total_change // DIME

Subtract the corresponding value from total_change:

    total_change -= dimes * DIME

Append the correct dime description to output_list:

    If dimes == 1, append "1 Dime"

Else, append "X Dimes"

Step 5.4: Compute Nickels

If total_change is greater than or equal to NICKEL, compute the number of nickels:

    nickels = total_change // NICKEL

Subtract the corresponding value from total_change:

    total_change -= nickels * NICKEL

Append the correct nickel description to output_list:

    If nickels == 1, append "1 Nickel"

Else, append "X Nickels"

Step 5.5: Compute Pennies
If total_change is greater than or equal to PENNY, compute the number of pennies:

    pennies = total_change // PENNY

Subtract the corresponding value from total_change:

    total_change -= pennies * PENNY

Append the correct penny description to output_list:

    If pennies == 1, append "1 Penny"

    Else, append "X Pennies"

Step 6: Display Output:
Convert output_list into a string and print it:
    - Example: print(" ".join(output_list))

Step 7: End Program */