# letters = ['a','b','c']
# print(letters[0])

# # WHILE LOOP
# count= 0

# while 5 > count:
#     print("Hello")
#     count = count+1

# name = input("What is your name?")
# while name != "Andrea":
#     print("I don't know you!")
#     name = input ("What is your name again?")



# for number in range(0,10):
#     print(number)

# students = [["Cindy", "Emily", "Eve"],
#             ["Julie", "Maddy", "Andrea"],
#             ["Jenny", "Sarah", "Yara"]
#             ]
# for student in students:
#     print(students)
#     for name in students:
#         print(name)


# In Python, elif is short for "else if" and is used when the first if statement isn't true, but you want to check for another condition. Meaning, if statements pair up with elif and else statements to perform a series of checks.



# if 5<3:
#     print("Hello")
# else:
#     if 1<=1:
#         print("Hi")
#     if 10==10:
#         print("How are you?")

#---------------------------------------#
##########EXERCISES######################

##Q1##

# number = (input("Enter a number: "))
# sum= 0 

# while number!= "":
#     number = int(number)
#     sum = sum + number
#     number= (input("Enter a number: "))
# print(f"Your numbers sum to {sum}")

### Q2###
# integer_number  = input("Please enter an integer number: ")
# integer_number = int(integer_number)
# for number in range(0,integer_number+1):
#     if number%2==1:
#         print(number)

##OTHER WAY TO DO IT:
# number =0
# integer_number  = input("Please enter an integer number: ")
# integer_number = int(integer_number)

# while number <integer_number:
#     if number%2==1:
#         print(number)
#     number=number+1

   ### Q3### 
# print("Guess a random number:")
# guessed_number= input("Make a guess: ")
# guessed_number= int(guessed_number)
# number = 9

# while guessed_number != number:
#     if guessed_number > number:
#         print("Too high...")
#     else:
#         print("Too low..")
#     guessed_number= input("Make a guess: ")
#     guessed_number= int(guessed_number)

# print("You got it right!")

   ### FOR LOOPS### 
####Q1#######
# user_number = input("Enter a number: ")
# user_number =int(user_number)

# for number in range(1,11):
#     print(f"{user_number} * {number} =  {user_number*number}")

####Q2#######
# user_number = input("Enter a number")
# user_number= int(user_number)
# sum = 0
# for number in range(0,user_number+1):
#     sum += number 
# print(sum)

#####Q3#########

# my_numbers = [3,4,5]

# sum=0
# for num in my_numbers:
#     sum+=num
# print(sum)


######Q4#########
# lyrics = [    ["Monica", "in my life"],
#             ["Erica", "by my side"],
#             ["Rita's", "all I need"],
#             ["Tina's", "what I see"],
#             ["Sandra", "in the sun"],
#             ["Mary", "having fun"],
#             ["Jessica", "here I am"]
#             ]

# for name in lyrics:
#     print(f"A little bit of {name[0]} {name[1]};")
# print("A little bit of you makes me your man (ah!)")
# print("*trumpet solo*")

######NESTED LOOPS###########
######Q1##############
# groceries = [    ["Baby Spinach", 2.78],    
#                 ["Hot Chocolate", 3.70],
#                 ["BBQ Shapes", 9.00],
#                 ["Bread", 2.10],
#                 ["Carrots", 0.56],
#                 ["Oranges", 3.08]
#                 ]

# quantity=[]
# total=0

# for item in groceries:
#     quantity_number = input(f"Please enter the quantity for {item[0]}:")
#     quantity_number = int(quantity_number)
#     total+=quantity_number
#     quantity.append(quantity_number)
 
# print(quantity)
# print(total)

##########Q2#####################
import random


# play = input("Would you like to guess a number? Y or N: ")
# while play == "Y":
#     number = random.randint(1,100)
#     print(number)
#     guessed_number= input("Make a guess: ")
#     guessed_number= int(guessed_number)

#     while guessed_number != number:
#         if guessed_number < number:
#             print("Too low...")
#         elif guessed_number > number:
#             print("Too high..")
#             guessed_number= input("Make a guess: ")
#             guessed_number= int(guessed_number)

#     print("You got it right!")
#     play = input("Would you like to play again? Y or N: ")
 
while number!= "":
    number = int(number)
    sum = sum + number
    number= (input("Enter a number: "))
print(f"Your numbers sum to {sum}")