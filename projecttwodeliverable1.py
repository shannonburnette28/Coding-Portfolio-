#Shannon Burnette
#Project 2 - Deliverable 1 
'''
Game of Life :Python edition

Algorithim

 Gameplay Flow
1. Have a Welcome and Instructions:
   - Display a welcome message and brief instructions about the game.

2. Character Creation:
   - Prompt the user to input their name.
   - Set the starting wealth to $1,000.

3. Choose Career Path:
   - Present two options: "Career" or "Education."
   - If "Education" is chosen:
     - Subtract $40,000 (student loan) from wealth initially.
     - Player starts from space 1 and goes through the first 10 education spaces.
   - If "Career" is chosen:
     - Start from space 11.

4. Career and Salary Setup:
   - Present a menu of careers based on the chosen path:
     - Education Careers: Professor, Engineer, Entrepreneur, Doctor (higher salary range).
     - Career Track Careers: Artist, Mechanic, Influencer (lower salary range).
   - Assign a random salary based on the career chosen:
     - Education Path Salary: Between $6,000 - $10,000 per pay period.
     - Career Path Salary: Between $3,000 - $6,000 per pay period.

5. Gameplay Mechanics:
   - Players roll a die to move spaces.
   - Pay Day occurs every 8 spaces, paying the player's assigned salary.

6. Board Events:
   - Upon landing on a non-Pay Day square, the player encounters a random event:
     - Unexpected Expenses.
     - Buy a House.
     - Win a Prize.
     - Family Milestone (Vacation or Baby).
     - Job Promotion.

7. Game Conclusion:
   - When the player reaches the final space:
     - Calculate the total wealth:
       - Subtract loans if applicable.
       - Add property values (with 50% increase).
     - Display the total wealth and a retirement message.



Function Specifications
Each function performs specific tasks and interacts with the main gameplay loop.

1. roll_die()
- Input: None.
- Output:Random integer between 1 and 6.
- Purpose: Determines the number of spaces a player moves or selects an event

2. board_events(position, wealth, salary, properties)
- Input: Player's current position, wealth, salary, and properties owned.
- Output: Updated values of wealth, position, or properties.
- Purpose:
  - Calls roll_die() to determine the event type.
  - Calls specific event functions based on the roll result:
    1. unexpected_expense()
    2. buy_house()
    3. win_prize()
    4. vacation()
    5. have_baby()
    6. promotion()

3. unexpected_expense(wealth)`**
- Input: Player's current wealth.
- Output: Updated wealth after deducting an expense.
- Purpose: Deducts a random amount ($100 - $1,000) based on an unforeseen cost.



4. buy_house(wealth, properties)
- Input: Player's current wealth and properties owned.
- Output: Updated wealth and property list.
- Purpose:
  - Displays a list of 2-3 houses with varying prices.
  - Allows the player to purchase if they have sufficient wealth.
  - Adds the property to the player's assets.

---

5. win_prize(wealth)
- Input:  Player's current wealth.
- Output: Updated wealth after adding a prize.
- Purpose: Adds a random amount ($100 - $1,000) based on winning a competition.


6. vacation(wealth)
- Input: Player's current wealth.
- Output: Updated wealth after deducting vacation costs.
- Purpose: Deducts $500 for a family vacation.


7. have_baby(wealth)
- Input: Player's current wealth.
- Output: Updated wealth.
- Purpose: Deducts $50 for hospital bills. Randomly determines gender (boy/girl).



8. promotion(salary)
- Input: Player's current salary.
- Output: Updated salary.
- Purpose: Increases salary by 10% and displays a promotion message.


9. calculate_total_wealth(wealth, properties)
- Input: Player's current wealth and properties owned.
- Output: Final wealth value after adjustments.
- Purpose:
  - Subtracts loans if applicable.
  - Adds 50% to the value of owned properties.



(Below) **Variable| **Type | **Description                                                
**name =str - Stores the player’s name.                                      
**wealth  = float -  Tracks the player’s current wealth.                           
**position = int  - Tracks the player’s current position on the board.    
**salary  =  float -  Stores the player’s salary based on the chosen career. 
**properties = list  - Stores the values of properties owned by the player.          
**board_size =  int  - Fixed value representing the number of spaces (100).



Mathematical and Input/Output Operations

1. Dice Rolling:
   - Formula: random.randint(1, 6).

2. Salary Increase (Promotion):
   - Formula: salary += salary * 0.1

3. **Property Value at Retirement:
   - Formula: `property_value += property_value * 0.5.

4. Wealth Adjustments:
   - Deduct or add wealth during events.

5. User Input:
   - Enter player name.
   - Choose between "Career" and "Education."
   - Select a house during the buy_house() event.



This algorithm outlines the gameplay mechanics and provides a detailed structure for how the functions should interact, the variables needed, and how the game progresses logical
