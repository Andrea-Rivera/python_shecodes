#Function : purpose of a thing
#input(), len(), int(), print()

# name = input("What is your name?")
# age=input("How old are you?")
# if age>=18:
#     print("Welcome")
# else:
#     print("You cannot enter")

# Task Separation
# def ask_user_name():
#     print("Function entered")
#     name = input("What is your name?")

# def ask_user_age():
#     age=int(input("How old are you?"))
#     if age>=18:
#         print("Welcome")
#     else:
#         print("You cannot enter")

# print("Hello")
# ask_user_name()
# ask_user_age()

###RETURN inmediately exit of the function so the rest 
##of the program will NOT be executed.

##PARAMETERS
# def add(number1, number2):
#     result = number1+number2
#     return result

# answer=add(2,3)
# print(answer)

###I NEED TO RETURN IF I WANT TO CATCH THE RESULT IN A VARIABLE
#####LOCAL VARIABLE: ONLY EXIST INSIDE THE BLOCK OF CODE . FOR EXAMPLE, RESULT IS A LOCAL VARIABLE.
####ASNWER IS A GLOBAL VARIABLE.

###EXERCISES####
##Q1##
# def get_integer(string):
#     number = int(string)
#     return number

# user_input = get_integer(input("Could I please have an integer?:"))
# print(f"So your integer is {user_input}. Thanks")


##Q2###
# def celcius_convert(number):
#     farenheit_number= float(number)
#     celsius  = (farenheit_number - 32) * .5556
#     return celsius

# print(f"{celcius_convert(350)} celcius")

####Q3########
def odd_number(number):
    if number%2==1:
        return True
    elif number%2==0:
        return False

print(f"{odd_number(7)}")

###Q4####
def groceries(price, quantity):
    price=float(price)
    quantity= int(quantity)
    return price * quantity

print(f"$ {groceries(1.49 , 7)}")
