'''
Shannon Burnette
november 19 2024
'''

def main():
    contacts = {"Stacey Y. Jones": "443-768-3979", "Britt J. Mosley": "443-826-0196",
                "Paula Jones": "443-629-0478", "Kyrsten N. Jones-Mosley": "443-814-5702",
                "Ashley Sierra Jones": "443-537-0630", "Tanya Casey":"516-519-0992",
                "Kayin Britt": "443-915-2931", "Shelly Mosley":"443-413-9279", "Dylan Plain":"410-413-0842", "Rashee Muhammad":"443-683-6206"}

    while True:
        print("\nMenu")
        print("1. Quit")
        print("2. See a list of people in the dictionary.")
        print("3. Print the entire dictionary.")
        print("4. Look up the value by giving the name.")
        print("5. Add a person to the dictionary.")
        print("6. Check if a person is in the dictionary.")
        print("7. Remove a person from the dictionary.")

        choice = input("Enter your choice:")

        if choice == "1":
            break
        elif choice == "2":
            for name in contacts.keys():
                print(name)
        elif choice == "3":
            for name, number in contacts.items():
                print(f"{name}:{number}")
        elif choice == "4":
            name = input("Enter the name:")
            if name in contacts:
                print(f"{name}:{contacts[name]}")
            else:
                print("Name not found in the dictionary.")
        elif choice == "5":
            name = input("Enter the new person's name:")
            number = input("Enter the telephone number:")
            contacts[name] = number
            print(f"{name} added to the dictionary.")
        elif choice == "6":
            name = input("Enter the name to check:")
            if name in conctacts:
                print(f"{name} is in the dictionary.")
            else:
                print(f"{name} is not in the dictionary.")
        elif choice == "7":
            name = input("Enter the name to remove:")
            if name in contacts:
                del contacts[name]
                print(f"{name} has been removed from the dictionary.")
            else:
                print("Name not found in the dictionary.")
        else:
            print("invalid choice. Please try again!")
            
main()
        
            
