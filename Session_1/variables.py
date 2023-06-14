
# #Strings
today= "Tuesday"
print(today)

# # # Numerical data types- Integer, Float
# # Integer - whole number
parkers_age = 4
print(type(parkers_age))
print (f"Parker is turning {parkers_age+1} soon!")
height = 155
print(f"My height is {height/100} in m.")


distance = "5000"
print(int(distance)+8)
print((distance)+str(8))

dog_name= input("What's the dog's name?")
print(f"Nice to meet you {dog_name}")

birth_year = input (f"What year you were born?")
print(f"You are {2023-int(birth_year)} years old")

##EXERCISES###
###Q1: Write a program that takes two numbers from the user,and outputs their sum
first_number  = input (f"Enter a number: ")
second_number  = input (f"Enter another number: ")
print(f" Result: {float(first_number) + float(second_number)}")

###Q2: Write a program that takes two numbers from the user,and outputs the equation representing the multiplication ofthe two numbers
first_number  = input (f"Enter a number: ")
second_number  = input (f"Enter another number: ")
print(f" Multiplication: {float(first_number) * float(second_number)}")

##Q3: Write a program that takes a distance in kilometers fromthe user, and output the distance in meters and centimeters.
# distance = input(f"How many kilometres: ")
distance_float = float(distance)
meters = distance_float*1000
print(f"the distance in meters is: {int(meters)}")
print(f"the distance in metres is : {int((float(distance)*1000))}m in centimetres is  {int(float(distance)*100000)}cm ")

##Q4: Write a program that takes the user's name and height(in centimeters), and outputs a summary sentence
name = input(f"What is your name? ")
height = input(f"How tall are you (cms)? ")
print(f"{name} is {height}cms tall ")
