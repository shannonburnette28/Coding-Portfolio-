/* Tossing Coins for a Dollar Game Algorithm:
 Shannon Burnette - 2/26/2025

Purpose of the Program: 
- The purpose of this program is so that it simulates a game where a player starts with a 
balance of $0 and tosses a virtual coin five times. 
- Each time the coin lands heads-up, a random amount of cents is added to the balance. 
- The game ends when the balance reaches or exceeds $1 or when all five tosses are used. 
- The player wins if the balance is exactly $1; otherwise, they lose.

                                   - Algorithm - 

Variables Used:
    balance (float): Stores the current balance in dollars.

    toss_count (int): Keeps track of the number of coin tosses.

    coin_result (string): Stores the result of the coin flip, either "Heads" or "Tails".

    added_amount (float): Stores the randomly generated cent value added to the balance.

Functions Used:
- random.randint(a, b): Generates a random integer between a and b.

- random.choice(["Heads", "Tails"]): Randomly selects "Heads" or "Tails".

- print(message): Displays output messages to the user.

Step-by-Step Process:

Import Required Libraries:
 (import random) -  to use random number generation functions.

Initialize Variables:
    - Set balance = 0.0 (starting balance in dollars).

    - Set toss_count = 0 (to keep track of tosses).

Start the Game Loop:

 - While toss_count < 5 and balance < 1.0: - this would be a while loop and the "and" would be a boolean operator. 

 - Increment toss_count by 1.

 - Generate coin_result = random.choice(["Heads", "Tails"]).

 - If coin_result == "Heads":

 - Generate added_amount = random.randint(1, 100) / 100 (convert cents to dollars).

 - Add added_amount to balance.

 - Print the toss result and updated balance.

 - Check Win/Loss Conditions:

 - If balance == 1.0: Print "You win!"

 - If balance > 1.0 or toss_count == 5: Print "You lose!"

    - Print the final balance. */ 