#Function : purpose of a thing
#input(), len(), int(), print()

name = input("What is your name?")
age=input("How old are you?")
if age>=18:
    print("Welcome")
else:
    print("You cannot enter")

# Task Separation
def ask_user_name():
    print("Function entered")
    name = input("What is your name?")

def ask_user_age():
    age=int(input("How old are you?"))
    if age>=18:
        print("Welcome")
    else:
        print("You cannot enter")

print("Hello")
ask_user_name()
ask_user_age()

###RETURN inmediately exit of the function so the rest 
##of the program will NOT be executed.

##PARAMETERS
def add(number1, number2):
    result = number1+number2
    return result

answer=add(2,3)
print(answer)

###I NEED TO RETURN IF I WANT TO CATCH THE RESULT IN A VARIABLE
#####LOCAL VARIABLE: ONLY EXIST INSIDE THE BLOCK OF CODE . FOR EXAMPLE, RESULT IS A LOCAL VARIABLE.
####ANSWER IS A GLOBAL VARIABLE.

###EXERCISES####
##Q1##
#Write a function called get_integer that takes a string as its argument, 
# and uses thatstring to prompt the user to enter an integer. 
# Your function should return the integersupplied by the user.

def get_integer(string):
    number = int(string)
    return number

user_input = get_integer(input("Could I please have an integer?:"))
print(f"So your integer is {user_input}. Thanks")


##Q2####
# Write a function called celcius_convert that takes a number representing 
# thetemperature in Farenheit as its argument, and returns a float 
# representing thetemperature in Celcius.
def celcius_convert(number):
    farenheit_number= float(number)
    celsius  = (farenheit_number - 32) * .5556
    return celsius

print(f"{celcius_convert(350)} celcius")

####Q3########
##Write a function that accepts one argument (an integer) and returns True 
# when thatargument is odd and False when that argument is even. 
# You can use the same formatas the starter code in the previous exercise. 
# Just remember - you're returning theresult, not printing it!
def odd_number(number):
    if number%2==1:
        return True
    elif number%2==0:
        return False

print(f"{odd_number(7)}")

###Q4####
#Write a function that takes two arguments; the unit price of an item, 
# and how manyunits were purchased. Return the total cost as a string

def groceries(price, quantity):
    price=float(price)
    quantity= int(quantity)
    return price * quantity

print(f"$ {groceries(1.49 , 7)}")

===========================================================================

def calculate_mean(weather_data):
    data_number=[]
    for number in weather_data:
        number=int(number)
        data_number.append(number)

    sum_data = sum( data_number)
    length_data = len( data_number)
    mean_weather_data= sum_data/length_data
    return mean_weather_data

print(calculate_mean(["51", "58", "59", "52", "52", "48", "47", "53"]))

