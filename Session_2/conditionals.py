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

    ##EXERCISES 
    ##  Q1

# sara_has_helmet = True

# if sara_has_helmet:
#     print("Let's send it!")
# else:
#     print ("No way, my brain is my moneymaker")


#    ##  Q2 #####
# sara_has_helmet = False
# rei_has_rope = False

# if sara_has_helmet and rei_has_rope:
#     print("Let's send it!")
# elif sara_has_helmet == False and rei_has_rope == True:
#     print("No way, my brain is my moneymaker!")
# elif sara_has_helmet==True and rei_has_rope==False:
#     print("Who's unprepared now. Rei?")
# elif sara_has_helmet==False and rei_has_rope==False:
#      print("I guess let's just go hiking?")

###### Q3 ######
light_color= 'Red'
car_detected = 'True'

if light_color=='Red'and car_detected == 'True':
    print("Flash")
else:
    print("Do nothing")

###### Q4 ######
# height_input = input("What is your height in cms?")
# height = int(height_input)

# if height >= 120:
#     print ("hop On")
# else:
#     print ("Sorry, not today")

name= input("What is your username?")
password = input("Whay is your password?")

correct_name = "lucyg"
correct_password = "quartzgleam?1"


if correct_name == name and correct_password == password:
    print("Logged in Successfully")
else:
    print ("Access denied")


email = input("Please enter your Email:")
if "@" and "." in email:
    print ("valid email")
else:
    print ("Invalid Email detected!")

#Q7#

if "False":
    print ("A strange game. The only winning move is not to play")

# Explanation: In this case, the string "False" is evaluated to True. From Google:
# In fact, except for empty strings, all the strings evaluate to True. Any number except 0, 
# evaluates to True. Moreover, apart from the empty ones, all the sets, lists, tuples, 
# and dictionaries also evaluate to True.andd
