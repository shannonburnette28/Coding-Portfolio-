#shannon burnette
#purpose : this is a program that pciks six distinct numbers from 1 to 36 for a lottery
#uses a set to avoid duplicates

import random

def main():
    numbers = set()
    while len(numbers) != 6:
                numbers.add(random.randint(1, 36))

  print (numbers)

main () 
