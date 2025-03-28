#Thisis program to count the frequencies of letters in an input string
#S.K. Burnette
def main():
    letters = {}
    toCount = input("Please enter a string to be counted")

    #use a loop to step through the string, one letter at a time
    for character in toCount:
        letters[character] = letters.get(letters,0) +1

        for key, value in letters.items():
            print(key, ' ', value, ' ', key * value)

main() 
