letters = ['a','b','c']
print(letters[0])

# # WHILE LOOP
count= 0

while 5 > count:
    print("Hello")
    count = count+1

name = input("What is your name?")
while name != "Andrea":
    print("I don't know you!")
    name = input ("What is your name again?")
print("Hi Andrea!")

##NESTED LOOPS

for number in range(0,10):
    print(number)

students = [["Cindy", "Emily", "Eve"],
            ["Julie", "Maddy", "Andrea"],
            ["Jenny", "Sarah", "Yara"]
            ]
for student in students:
    print(students)
    for name in students:
        print(name)


# In Python, elif is short for "else if" and is used when the first if statement isn't true, but you want to check for another condition. Meaning, if statements pair up with elif and else statements to perform a series of checks.

if 5<3:
    print("Hello")
else:
    if 1<=1:
        print("Hi")
    if 10==10:
        print("How are you?")

#---------------------------------------#
##########EXERCISES######################

##Q1##
#Continuously ask the user to enter a number until they provide a blank input. 
# Outputthe sum of all the numbers.

number = (input("Enter a number: "))
sum= 0 

while number!= "":
    number = int(number)
    sum = sum + number
    number= (input("Enter a number: "))
print(f"Your numbers sum to {sum}")

### Q2###
#Ask the user to enter a in integer number. 
# Print all the odd numbers between 0 andthat number (inclusive). 

integer_number  = input("Please enter an integer number: ")
integer_number = int(integer_number)
for number in range(0,integer_number+1):
    if number%2==1:
        print(number)

##OTHER WAY TO DO IT:
number =0
integer_number  = input("Please enter an integer number: ")
integer_number = int(integer_number)

while number <integer_number:
    if number%2==1:
        print(number)
    number=number+1

### Q3### 
#Select a number, and save it as a variable in your code. 
# Ask the user to enter anumber, and then output whether their number 
# is less than or greater than theselected number. 
# Keep asking until the user guesses the correct number. 
# Then print acongratulatatory message.

print("Guess a random number:")
guessed_number= input("Make a guess: ")
guessed_number= int(guessed_number)
number = 9

while guessed_number != number:
    if guessed_number > number:
        print("Too high...")
    else:
        print("Too low..")
    guessed_number= input("Make a guess: ")
    guessed_number= int(guessed_number)

print("You got it right!")

   ### FOR LOOPS### 
####Q1#######
#Ask the user for a number. Use a for loop to print the times 
# tables for that number,up to ten.

user_number = input("Enter a number: ")
user_number =int(user_number)

for number in range(1,11):
    print(f"{user_number} * {number} =  {user_number*number}")

####Q2#######
#Ask the user for an integer. Using a for loop, add up every number 
# from 0 up to thatinteger, and print the result.
user_number = input("Enter a number")
user_number= int(user_number)
sum = 0
for number in range(0,user_number+1):
    sum += number 
print(sum)

#####Q3#########
##Save a list of numbers to a variable in your script,
#  and then use a for loop to print thesum of all the numbers in the list.

my_numbers = [3,4,5]

sum=0
for num in my_numbers:
    sum+=num
print(sum)


######Q4#########
#Let's improve our Mambo No. 5 code from the last block of content.
# Save the following variable in your code:

lyrics = [    ["Monica", "in my life"],
            ["Erica", "by my side"],
            ["Rita's", "all I need"],
            ["Tina's", "what I see"],
            ["Sandra", "in the sun"],
            ["Mary", "having fun"],
            ["Jessica", "here I am"]
            ]

#Then use a for loop to print out the following text:

for name in lyrics:
    print(f"A little bit of {name[0]} {name[1]};")
print("A little bit of you makes me your man (ah!)")
print("*trumpet solo*")

######NESTED LOOPS###########

######Q1#############
# Below is a list of grocery items and their prices per unit:

groceries = [    ["Baby Spinach", 2.78],    
                ["Hot Chocolate", 3.70],
                ["BBQ Shapes", 9.00],
                ["Bread", 2.10],
                ["Carrots", 0.56],
                ["Oranges", 3.08]
                ]
#Ask the user how many units of each item they bought, 
# then output the correspondingreceipt. 

quantity=[]
total=0

for item in groceries:
    quantity_number = input(f"Please enter the quantity for {item[0]}:")
    quantity_number = int(quantity_number)
    total+=quantity_number
    quantity.append(quantity_number)
 
print(quantity)
print(total)

##########Q2#####################
#Let's improve the guessing game you wrote in Q3 of the while loop exercises. 
# Updatethe code so that when the game ends, the program asks the player if 
# they would liketo play again. If they input "no", the game ends, 
# but with any other input the gamebegins again.

import random


play = input("Would you like to guess a number? Y or N: ")
while play == "Y":
    number = random.randint(1,100)
    print(number)
    guessed_number= input("Make a guess: ")
    guessed_number= int(guessed_number)

    while guessed_number != number:
        if guessed_number < number:
            print("Too low...")
        elif guessed_number > number:
            print("Too high..")
            guessed_number= input("Make a guess: ")
            guessed_number= int(guessed_number)

    print("You got it right!")
    play = input("Would you like to play again? Y or N: ")
