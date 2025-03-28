#Shannon Burnette
#November 26th 2024
#This is project deliverable three, the purpose of this code is to simulate the game of life through python code 

import random

# Function to roll the die
def roll_die():
    return random.randint(1, 6)

# Welcome Message and Instructions
def welcome():
    print("Welcome to the Game of Life!")
    print("Your goal is to navigate through the board, manage your wealth, and make decisions.")
    print("Every space has an event. Try to retire with as much wealth as possible!")
    print()

# Character Creation
def create_character():
    name = input("Enter your character's name: ")
    wealth = 1000
    print(f"\nWelcome, {name}! You start the game with ${wealth}.")
    return name, wealth

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

# Board Event Logic
def handle_event(position, wealth):
    events = [
        ("You found a bonus opportunity! Gain $500.", 500),
        ("You got a flat tire. Pay $200.", -200),
        ("You helped a friend move and earned $300.", 300),
        ("You had to pay for an unexpected medical bill. Lose $400.", -400),
        ("You invested in a stock and gained $600.", 600),
        ("You treated yourself to a vacation. Lose $300.", -300),
        ("You received a gift from a relative. Gain $250.", 250),
        ("Your car broke down. Pay $500.", -500),
        ("You attended a free seminar and gained knowledge!", 0),
        ("You were fined for speeding. Pay $150.", -150),
    ]
    event, change = random.choice(events)
    print(f"Event on space {position}: {event}")
    wealth += change
    print(f"Current Wealth: ${wealth}")
    return wealth

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

        # Handle board events
        wealth = handle_event(position, wealth)

        # Pay Day Logic
        if position % pay_day_interval == 0 or (position // pay_day_interval > (position - roll) // pay_day_interval):
            print("It's Pay Day! You receive your salary.")
            wealth += salary
            print(f"Current Wealth: ${wealth}")
    
    return wealth

# Retirement Overview
def retirement_summary(name, wealth):
    print(f"\n{name}, you've reached retirement!")
    print(f"Your final wealth is ${wealth}.")
    if wealth >= 100000:
        print("You retired as a millionaire! Congratulations on a life well-lived!")
    elif wealth >= 50000:
        print("You retired comfortably. Great job managing your life choices!")
    else:
        print("Retirement is a bit tight, but you made it! Reflect on your journey.")
    print("Thank you for playing the Game of Life!")

# Main Function
def main():
    welcome()
    name, wealth = create_character()
    path = choose_path()
    career, salary = choose_career(path)
    final_wealth = game_loop(path, name, wealth, salary)
    retirement_summary(name, final_wealth)

# Run the Program
if __name__ == "__main__":
    main()
