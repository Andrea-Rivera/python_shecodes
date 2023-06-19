
# Dictionary
# Keys are unique
# Values can be any data type
# Keys can only be immutable data types 
# Immutable - Strings, integers, floats, booleans
student_phonebook = {
    "Cindy":111,
    "Tracey":123,
    "Pauline":444
    }
print(student_phonebook)
#To delete records from the dictionary
del student_phonebook["Tracey"]
#To change records from the dictionary
student_phonebook["Cindy"] = 555
print(student_phonebook)
student_phonebook["Yara"] = 555
print(student_phonebook)
print(type(student_phonebook))
student_phonebook["Andrea"] = 345
print(student_phonebook)

dictionary_empty = {}
dictionary_empty['loop'] = "the action of doing something over and over agan"
print(dictionary_empty)

print("---------------------------------")
# Iterate all the values in a dictionary
# for value in student_phonebook.values():
#     print(value)

# Iterate all the key-value pairs
# for key in student_phonebook:
#     print(key, student_phonebook[key])

# a,b,c = [1,2,3]
# print(a)
# print(b)
# print(c)

# for key,value in student_phonebook.items():
#     print(key,value)


###########EXERCISES ####################################

########### Q1 ##################
print("########  Q1 ######################")
##The dictionary below represents the cost of individual items in a supermarket. 
# Write aprogram that asks the user how many of each item they would like in turn, 
# and outputsthe total cost of their groceries.

groceries = {"Baby Spinach": 2.78,
             "Hot Chocolate": 3.70,
             "Crackers": 2.10,
             "Coffee": 9.00,
             "Carrots": 0.56,
             "Oranges": 3.08}


total=0
for key,value in groceries.items():
    amount=input(f"How many {key} do you want?")
    # print(type(quantity))
    # print(type(value))
    #print('-------')
    #print(key, value, amount)
    item_value=(value*int(amount))
    print(item_value)
    total+=item_value
print(total)

print("---------------------------------")

########### Q2 ##################
##Write this program so that instead of using separate variables 
# to keep track of the number of times each colour name appears, 
# it uses a single dictionary instead.
# Here's a dictionary to get you started:
print("########  Q2 ######################")
import csv

colour_counts = {"blue": 0,"green": 0,"yellow": 0,"red": 0,"purple": 0,"orange": 0,}

with open("Session7/colours_865.csv", encoding="utf-8") as colours:

    reader = csv.reader(colours)
   # loop time!
    for colour in reader:

    # Each row in the data gets converted into a list.
        english_colour= colour[2].lower()
        #print(english_colour)
        if "blue" in english_colour:
            colour_counts["blue"] = colour_counts["blue"]+1
        if "green" in english_colour:
            colour_counts["green"] = colour_counts["green"]+1
        if "yellow" in english_colour:
            colour_counts["yellow"] = colour_counts["yellow"]+1
        if "red" in english_colour:
            colour_counts["red"] = colour_counts["red"]+1
        if "orange" in english_colour:
            colour_counts["orange"] = colour_counts["orange"]+1
        
    print(colour_counts)

    print("---------------------------------")

########### Q3 ##################
#Read the colour data from colours_20_simple.csv (available in the repo linked above)and save the data 
# in a dictionary where each key is a hex code and each value is thecorresponding English name.

print("########  Q3 ######################")
with open("Session7/colours_20_simple.csv", encoding="utf-8") as colours:
    colour_dictionary = {}

    reader = csv.reader(colours)
   # loop time!
    for colour in reader:
        key=colour[1]
        value=colour[2]

        colour_dictionary[key]=value
    print(colour_dictionary)
    print("----------------------------------")
    
########### Q4 ##################
##Modify your code from the previous exercise to save both the English name and RGBcode in a list as the value for the corresponding hex code.
print("########  Q4 ######################")
with open("Session7/colours_20_simple.csv", encoding="utf-8") as colours:
    colour_dictionary = {}

    reader = csv.reader(colours)
   # loop time!
    for colour in reader:
        key=colour[1]
        value1=colour[0]
        value2=colour[2]

        colour_dictionary[key]=[value1, value2]
    print(colour_dictionary)
    print("----------------------------------")

