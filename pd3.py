# S. K. Burnette
# This program welcomes the user, presents a menu, allows a choice, 
# adds extra services based on restrictions, and calculates the total including a tip.

# Initialize total cost, selected services list, and extra services list
total_cost = 0
selected_services = ""
extra_services = ""

# Display the salon welcome message
print("Welcome to the Beauty Salon!")

# Display the main menu of services
print("Please select one of our signature styles:")
print("1. Around the Way Curl ($55.99)")
print("2. Silk Press ($65.50)")
print("3. Two-Strand Twists ($85.00)")
print("4. Wash and Go ($55.99)")
print("5. Crochet Faux Locs ($199.99)")

# Get the user's choice
choice = input("Selection (1-5): ")

# Set the service cost and service name based on user's selection
if choice == '1':
    service_cost = 55.99
    service_name = "Around the Way Curl"
elif choice == '2':
    service_cost = 65.50
    service_name = "Silk Press"
elif choice == '3':
    service_cost = 85.00
    service_name = "Two-Strand Twists"
elif choice == '4':
    service_cost = 55.99
    service_name = "Wash and Go"
elif choice == '5':
    service_cost = 199.99
    service_name = "Crochet Faux Locs"
else:
    print("Invalid selection. Exiting the program.")
    exit()

# Add the selected style to the total cost and selected services
total_cost += service_cost
selected_services = f"Style: {service_name} (${service_cost:.2f})"

print(f"You've selected {service_name}")

# Start the extra services selection loop
while True:
    print("\nFeel free to add extra services.")
    print("1. Trim (requires Two-Strand Twists or Silk Press) ($15)")
    print("2. Deep conditioning mask ($20)")
    print("3. Detangling ($15)")
    print("4. Steam treatment (requires Around the Way Curl or Wash and Go) ($35)")
    print("5. Take down service (requires Crochet Faux Locs) ($50)")
    print("6. Done")

    extra_choice = input("Any Extras? (1-6): ")

    if extra_choice == '1':
        # Trim requires Two-Strand Twists or Silk Press
        if choice == '2' or choice == '3':
            total_cost += 15
            extra_services += "Extra: Trim ($15)"
            print("You've added Trim")
        else:
            print("This extra is only available with the Two-Strand Twists or Silk Press")
    elif extra_choice == '2':
        total_cost += 20
        extra_services += "Extra: Deep conditioning mask ($20)"
        print("You've added Deep conditioning mask")
    elif extra_choice == '3':
        total_cost += 15
        extra_services += "Extra: Detangling ($15)"
        print("You've added Detangling")
    elif extra_choice == '4':
        # Steam treatment requires Around the Way Curl or Wash and Go
        if choice == '1' or choice == '4':
            total_cost += 35
            extra_services += "Extra: Steam treatment ($35)"
            print("You've added Steam treatment")
        else:
            print("This extra is only available with the Around the Way Curl or Wash and Go")
    elif extra_choice == '5':
        # Take down service requires Crochet Faux Locs
        if choice == '5':
            total_cost += 50
            extra_services += "Extra: Take down service ($50)"
            print("You've added Take down service")
        else:
            print("This extra is only available with the Crochet Faux Locs")
    elif extra_choice == '6':
        break  # Exit the loop when the user is done selecting extras
    else:
        print("Invalid selection. Please try again.")

# Display the subtotal before tip
print(f"Your subtotal is: ${total_cost:.2f}")

# Prompt the user for a tip amount
tip = float(input("Please enter your tip amount: $"))

# Add the tip to the total cost
final_total = total_cost + tip

# Print the final bill in a neat, formatted manner
print("**********Your receipt**********")
print(selected_services)
if extra_services:
    print(extra_services.strip())  # Print any extra services selected
print(f"Tip: ${tip:.2f}")
print(f"Total: ${final_total:.2f}")
print("*******************************")

# Thank the user for visiting the salon
print("Thank you for visiting the Beauty Salon!")
