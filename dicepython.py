'''
import random
ask user how many times to run the simulation
generate two numbers for die1 and die2
count how many times each side comes up in a dictionary
Lets initialize the dictionaries first
loop creating randoms numbers and adding them to the dictionary
'''
def main():
    import random
    Die1 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    Die2 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    HowMany = int(input("how many times do you want to throw the dice?"))

    for X in range (HowMany):
         D1 = random.randint(1,6)
         D2 = random.randint(1,6)
         print ("the first dice is ", D1, "the second dice is ", D2) 
         Die1[D1] += 1
         Die2[D2] += 2
    print("Here is Dice number one") 
    for key, value in Die1.items():
        print (key, " ", value)
    print("Here is Dice number two")
    for key, value in Die2.items ():
        print(key, " ", value)
    freqDie1 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    freqDie2 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
  
main() 
