# S. K. Burnette
# This is a program that welcomes the user, presents a menu, allows a choice,
# and calculates the total cost including a tip.

# Initialize total cost and selected services list
total_cost = 0
selected_services = ""

# Display the salon welcome message
print("Welcome to the Beauty Salon!")

# Start a loop to allow multiple service selections until "Done" is selected
while True:
    # Display the menu of services
    print("Menu of Services")
    print("1. Around the Way Curl - $50")
    print("2. Silk Press - $60")
    print("3. Two-Strand Twists - $70")
    print("4. Wash and Go - $40")
    print("5. Crochet Faux Locs - $80")
    print("6. Done (Select this to finish your selection)")

    # Prompt user to enter their choice
    choice = input("Please select a service (1-6): ")

    # Set the service cost to zero initially
    service_cost = 0

    # Determine the service and cost based on user choice
    if choice == '1':
        service_cost = 50
        service_name = "Around the Way Curl"
        selected_services += f"{service_name} - $50"
    elif choice == '2':
        service_cost = 60
        service_name = "Silk Press"
        selected_services += f"{service_name} - $60"
    elif choice == '3':
        service_cost = 70
        service_name = "Two-Strand Twists"
        selected_services += f"{service_name} - $70"
    elif choice == '4':
        service_cost = 40
        service_name = "Wash and Go"
        selected_services += f"{service_name} - $40\n"
    elif choice == '5':
        service_cost = 80
        service_name = "Crochet Faux Locs"
        selected_services += f"{service_name} - $80\n"
    elif choice == '6':
        # Exit the loop if the user selects "Done" and has selected at least one service
        if total_cost == 0:
            print("You didn't select any services. Exiting.")
            exit()  # End the program if no services were selected
        break  # Exit the loop when "Done" is selected
    else:
        print("Invalid choice. Please select a number between 1 and 6.")
        continue  # Restart the loop if the input is invalid

    # Add the selected service's cost to the total cost
    total_cost += service_cost

# After exiting the loop, prompt the user for a tip percentage
tip_percentage = float(input("Enter the tip percentage (e.g., 10 for 10%): "))

# Calculate the tip amount based on the total service cost
tip_amount = total_cost * (tip_percentage / 100)

# Calculate the final total cost (service cost + tip)
final_total_cost = total_cost + tip_amount

# Display the selected services, total cost, tip, and final amount due
print("Summary of services selected:")
print(selected_services)
print(f"Total Service Cost: ${total_cost:.2f}")
print(f"Tip: ${tip_amount:.2f}")
print(f"Total Amount Due: ${final_total_cost:.2f}")

# Thank the user for visiting the salon
print("\nThank you for visiting the Beauty Salon!")
