#Shannon Burnette
#group project lab 

#main fucntion
#set the choice eqaul to zero
#print the main menu of the calculator so the user can input their choice of math
#give them the space to do so as well
choice = 0
while choice != 8:
    print("Welcome and thank you for using Cool Calc please pick one")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiplacation")
    print("4. Divison")
    print("5. Square Root")
    print("6. Exponent")
    print("7. Absolute Value")
    print("8. Exit")
    choice = int(input("Please enter an integer to make your choice:")) 
    num1 = float(input("Please enter one number"))
if choice == 1:
    num2 = float(input("Please enter a second number"))
    Sum = add (num1,num2)
    print('f Your sum is {Sum}')
elif choice == 2:
    num2 = float(input("Please enter a 2nd number:"))
    difference = subtract (num1, num2)
    print(f'Your difference is: {difference}')
elif choice == 3:
    num2 = float(input("Please enter a 2nd number:"))
    product = multiply (num1, num2)
    print(f'Your product is {product}')
elif choice == 4:
    num2 = float(input("Please enter a 2nd number:"))
    quotient = divide (num1, num2)
    print(f' Your quotient is: {quotient}')
elif choice == 5:
    root = sqrtroot (num1, num2)
    print(f' Your root is {root}')
elif choice == 6:
    num2 = float(input("Please enter a second number:"))
    answer = raisetoapower (num1, num2)
    print (f' Your answer is {answer}.') 
elif choice == 7:
    (num1) < 0
    absolute = num1 * -1
    print(f' Your absoltue value is: {absolute}') 
elif choice == 8:
    print("Thank you for using this calculator.") 
else:
    print("Enter a valid number.")
 #tells the defined fucntion what to do and also calls the function 
# each function recives 2 (#)'s from the main
def add (num1, num2):
    sum = num1 + num2
    return sum

add()

def subtract (num1, num2):
    return(num1 - num2)

subtract()

def multiply (num1, num2):
    answer = num1 * num2
    return answer

multiply()

def divide (num1, num2):
    if num2 == 0:
        return "error"
    else:
        quotient = num1/num2
        return quotient

divide()

def sqrtroot (num1):
    sqrt = num1 ** 0.5
    return sqrtroot

sqrtroot()


def raisetoapower (num1,num2):
    power = num1 ** num2
    return raisetoapower

rasietoapower()

def absolute (num1):
    if (num1) < 0:
        x = num1 * -1
        return x
    else:
        x = num1
        return x

absolute()

main() 
