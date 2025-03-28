#shannon burnette
#capitals testing program
#december 3 2024 
import random 
capitals = {'Alabama':'Montgomery','Alaska':'Juneau',
'Arizona':'Phoenix','Arkansas':'Little Rock',
'California':'Sacramento','Colorado':'Denver',
'Connecticut':'Hartford','Delaware':'Dover',
'Florida':'Tallahassee','Georgia':'Atlanta',
'Hawaii':'Honolulu','Idaho':'Boise',
'Illinois':'Springfield','Indiana':'Indianapolis',
'Iowa':'Des Moines','Kansas':'Topeka',
'Kentucky':'Frankfort','Louisiana':'Baton Rouge',
'Maine':'Augusta','Maryland':'Annapolis',
'Massachusetts':'Boston','Michigan':'Lansing',
'Minnesota':'Saint Paul','Mississippi':'Jackson',
'Missouri':'Jefferson City','Montana':'Helena',
'Nebraska':'Lincoln','Nevada':'Carson City',
'New Hampshire':'Concord','New Jersey':'Trenton',
'New Mexico':'Santa Fe','New York':'Albany',
'North Carolina':'Raleigh','North Dakota':'Bismarck',
'Ohio':'Columbus','Oklahoma':'Oklahoma City',
'Oregon':'Salem','Pennsylvania':'Harrisburg',
'Rhode Island':'Providence','South Carolina':'Columbia',
'South Dakota':'Pierre','Tennessee':'Nashville',
'Texas':'Austin','Utah':'Salt Lake City',
'Vermont':'Montpelier','Virginia':'Richmond',
'Washington':'Olympia','West Virginia':'Charleston',
'Wisconsin':'Madison','Wyoming':'Cheyenne'}

print("Welcome to my quiz program. I will ask you 10")
numRight = 0
numWrong = 0
states = list(capitals.keys())
print(states)
print(states[21])
for X in range (10):
    state = random.choice(states)
    guess = input(f"what is the capital of {state}?" )
    if guess.lower() == capitals[state].lower():
        print("Your are smart!")
        numRight += 1

    else:
        print(f"The answer was {capitals[state]} sorry!")
        numWrong += 1

print(f"you got {numRight} right and {numWrong} wrong") 
    
        
