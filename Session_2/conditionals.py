my_variable = True
my_variable2 = False
is_raining = True
print(my_variable)
print(type(my_variable))

#Comparison Operators
# == is equal to
# != not equal to 
# > greater than
# < less than

print(5>3)
print (3.5 > 6.3)
print("Asli" == "Asli")

# Mathematicla Operators 
# Addition
# Substraction
# Multiplication
# Division

is_sunny  = True
is_warm  = True
print (not is_sunny)
print (is_sunny and is_warm)

temperature = 18 

if temperature >= 18:
    print ("Weather is too cold")

# IF I NEED TO CHECK OTHER CONDITIONS
elif temperature > 28: # IF STATEMENT FALSE , IT WILL  CHECK ELIF
    print ("Weather is too hot")
# MULTIPLE IF STATEMENTS 
else : # will catch any other condition
    print ("weather is nice!")


    ########################################EXERCISES #####################################
    
    ##  Q1#####
    ##Sara is a confident rock climber, but sometimes she forgets her helmet.
    #  Rei refuses toclimb with Sara unless she's wearing a helmet, because That's Just Sensible.
    # Write a program that sets the value for a boolean variable called sara_has_helmet, 
    # andthen prints out a string indicating whether or not Rei is down to climb

sara_has_helmet = True

if sara_has_helmet:
    print("Let's send it!")
else:
    print ("No way, my brain is my moneymaker")


###  Q2 #####
##Rei is a very careful climber, but sometimes she is forgetful.
#  Even if Sara has a helmet,they still can't go climbing unless Rei remembers to bring her rope.
# Amend the previous program to add a check for the rope before you output the result.
sara_has_helmet = False
rei_has_rope = False

if sara_has_helmet and rei_has_rope:
    print("Let's send it!")
elif sara_has_helmet == False and rei_has_rope == True:
    print("No way, my brain is my moneymaker!")
elif sara_has_helmet==True and rei_has_rope==False:
    print("Who's unprepared now. Rei?")
elif sara_has_helmet==False and rei_has_rope==False:
    print("I guess let's just go hiking?")

###### Q3 ######
##Write a program that implements the algorithm for red light cameras. 
# The programshould print the string "Flash!" if (and only if) a car is detected 
# driving while the lightis red. If the light is green or amber, 
# the program should print "Do nothing.", even when a car is detected
light_color= 'Red'
car_detected = 'True'

if light_color=='Red'and car_detected == 'True':
    print("Flash")
else:
    print("Do nothing")

###### Q4 ######
##Write a program that asks the user for their height, and determines whether or notthey are tall enough to ride the rollercoaster,
#  which has a height requirement of120cms.

height_input = input("What is your height in cms?")
height = int(height_input)

if height >= 120:
    print ("hop On")
else:
    print ("Sorry, not today")

####Q5#########
##Write a program that asks the user to enter their username and password and output asuccess message if they are correct,
## or a failure message if they are incorrect. Yourprogram has one user, whose username is "lucyg", and whose password is "quartzgleam?1"

name= input("What is your username?")
password = input("What is your password?")

correct_name = "lucyg"
correct_password = "quartzgleam?1"

if correct_name == name and correct_password == password:
    print("Logged in Successfully")
else:
    print ("Access denied")

####Q6##########
####Write a program that asks the user to enter their email address and checks whether itis valid or not.
#  For the purpose of this exercise, you can make the assumption that anemail address is valid if it contains a “@” symbol and a “.” symbol.

email = input("Please enter your Email:")
if "@" and "." in email:
    print ("valid email")
else:
    print ("Invalid Email detected!")


