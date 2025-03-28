#S. K. Burnette
#This is a program that welcomes the user,
#(cont.) presents a menu, allows a choice, and calculates the cost including a tip.
#set choice = zero
choice = 0 
# display the salon welcome message
print("Welcome to the Beauty Salon!")
# Display the menu of services
#Include the service as well as the price for each one in numerical order 
print("Menu of Services")
print("1. Around the Way Curl - $50")
print("2. Silk Press - $60")
print("3. Two-Strand Twists - $70")
print("4. Wash and Go - $40")
print("5. Crochet Faux Locs - $80")
# Prompt user to enter their choice
choice = input("Please select a service (1-5): ")
# set the service cost to zero 
service_cost = 0
# Create a series of if/elif/else statements for the program
#(cont.) to determine the cost based on user choice
if choice == '1':
    service_cost = 50
    service_name = "Around the Way Curl" #make sure that after the price for each choice is established that the value is assigned a service 
elif choice == '2':
    service_cost = 60
    service_name = "Silk Press"
elif choice == '3':
    service_cost = 70
    service_name = "Two-Strand Twists"
elif choice == '4':
    service_cost = 40
    service_name = "Wash and Go"
elif choice == '5':
    service_cost = 80
    service_name = "Crochet Faux Locs"
#if the user enters none of the options 1 through 5 display an error message
else:
    print("Invalid choice. Please run the program again and select a number between 1 and 5.")
    exit() #create a function that will end the loop so we can calculate the service and tip
# Display the selected service and cost with an "f" string, 2 decimal places
print(f"You selected: {service_name} - ${service_cost:.2f}")
# Prompt the user for a tip percentage
#assign the tip percentage to the users float input
tip_percentage = float(input("Enter the tip percentage (e.g., 10 for 10%): "))
#assign the final tip amount to the equation of the cost of the serivice multiplied by the tip percentage
#dont forget to divide the percentage by 100
tip_amount = service_cost * (tip_percentage / 100)
# Calculate the total cost of the service and the tip and assign it to a total cost variable
total_cost = service_cost + tip_amount
# use "f" strings to display the results
print(f"Service Cost: ${service_cost:.2f}")
print(f"Tip: ${tip_amount:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
# End of the program thank the user for coming to the salon 
print("Thank you for visiting the Beauty Salon!")
