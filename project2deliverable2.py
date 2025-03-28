import random

# Function to roll the die
def roll_die():
    return random.randint(1, 6)

# Welcome Message and Instructions
def welcome():
    print("Welcome to the Game of Life!")
    print("Your goal is to navigate through the board, manage your wealth, and make decisions.")
    print("Reach the final space with as much wealth as possible!")
    print()

# Character Creation
def create_character():
    name = input("Enter your character's name: ")
    wealth = 1000
    print(f"\nWelcome, {name}! You start the game with ${wealth}.")
    return name, wealth
#Shannon burnette
#November 16 2024
#Project 2 - deliverable 2 
# Choose Path: Education or Career
def choose_path():
    print("\nChoose your path:")
    print("1. Education (Start with -$40,000 student loan, higher salary range)")
    print("2. Career (No loan, lower salary range)")
    choice = input("Enter 1 for Education or 2 for Career: ")
    while choice not in ['1', '2']:
        choice = input("Invalid choice. Enter 1 for Education or 2 for Career: ")
    return "Education" if choice == '1' else "Career"

# Career Selection
def choose_career(path):
    if path == "Education":
        print("\nChoose a career:")
        print("1. Professor")
        print("2. Engineer")
        print("3. Entrepreneur")
        print("4. Doctor")
        careers = ["Professor", "Engineer", "Entrepreneur", "Doctor"]
        salary_range = (6000, 10000)
    else:
        print("\nChoose a career:")
        print("1. Artist")
        print("2. Mechanic")
        print("3. Influencer")
        careers = ["Artist", "Mechanic", "Influencer"]
        salary_range = (3000, 6000)

    choice = int(input("Enter the number of your chosen career: "))
    while choice < 1 or choice > len(careers):
        choice = int(input("Invalid choice. Enter the number of your chosen career: "))
    
    career = careers[choice - 1]
    salary = random.randint(*salary_range)
    print(f"\nYou chose to be a {career} with a salary of ${salary} per pay period.")
    return career, salary

# Game Progression
def game_loop(path, name, wealth, salary):
    position = 0
    board_size = 100
    pay_day_interval = 8

    if path == "Education":
        wealth -= 40000
        print("\nYou chose the Education path. $40,000 student loan deducted from your wealth.")
        print(f"Current Wealth: ${wealth}\n")

    while position < board_size:
        input(f"{name}, press Enter to roll the die.")
        roll = roll_die()
        position += roll

        if position >= board_size:
            print(f"\nCongratulations! You have reached the final space!")
            break

        print(f"\nYou rolled a {roll} and moved to space {position}.")

       # Pay Day Logic
        if position % pay_day_interval == 0 or (position // pay_day_interval > (position - roll) // pay_day_interval):
            print("It's Pay Day! You receive your salary.")
            wealth += salary
            print(f"Current Wealth: ${wealth}")
        else:
            print(f"Current Wealth: ${wealth}")
    
    return wealth

# Main Function
def main():
    welcome()
    name, wealth = create_character()
    path = choose_path()
    career, salary = choose_career(path)
    final_wealth = game_loop(path, name, wealth, salary)
    print(f"\n{name}, you completed the game with a final wealth of ${final_wealth}.")
    print("Thank you for playing the Game of Life!")

# Run the Program
if __name__ == "__main__":
    main()
