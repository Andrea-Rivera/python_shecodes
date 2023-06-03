# Store multiple data points
# list_name = [1,2,3,"Asli", []]
# print(list_name)
# print (type(list_name))


digits=[1,2,3,4,5]
# print(digits[4])

# #Slicing
# print(digits[0:5])
# print(digits[0:5:2])

# # len
# print(len(digits))

# # adding elements
# digits.append(6)
# print(digits)

# pop in the index you want to remove. By default is will remove the last index
# digits.pop()
# print(digits)


# popped_element  = digits.pop(0)
# print (digits)
# digits.pop(0)
# print(digits)

####NESTED LIST
letters = ["a","b","c","d", ["Emily", "Julie"]]
print(len(letters))
print (letters[4])
print (letters[4][0])

if 'a' in letters:
    print("It is in the list")


##LIST EXERCISES#####
foods = ["orange",
         "apple",
         "banana",
         "strawberry",
         "grape",
         "blueberry",    
         ["carrot", "cauliflower", "pumpkin"],
         "passionfruit",
         "mango",
         "kiwifruit"
         ]

print("FOOD EXERCISE")
print (foods[0])
print (foods[2])
print (foods[-1])
print(foods[0:3])
print(foods[-3:10])
print(foods[6][-1])


####    Q2#####
mambo = [ ["Monica", "in my life"],    
 ["Erica", "by my side"],    
 ["Rita's", "all I need"],    
 ["Tina's", "what I see"],    
 ["Sandra", "in the sun"],    
 ["Mary", "having fun"],    
 ["Jessica", "here I am"]]

print (f"A little bit of {mambo[0][0]} {mambo[0][1]}")
print (f"A little bit of {mambo[1][0]} {mambo[1][1]}")
print (f"A little bit of {mambo[2][0]} {mambo[2][1]}")
print (f"A little bit of {mambo[3][0]} {mambo[3][1]}")
print (f"A little bit of {mambo[4][0]} {mambo[4][1]}")
print (f"A little bit of {mambo[5][0]} {mambo[5][1]}")
print (f"A little bit of {mambo[6][0]} {mambo[6][1]}")
print("A little bit of you makes me your man (ah!)")
print("*trumpet solo*")

####  Q3#####

name1 = input ("Please enter a name: ")
name2 = input ("Please enter second a name: ")
name3  = input ("Please enter a third name: ")

names=[]
names.append(name1)
names.append(name2)
names.append(name3)
print (names)

######Q4###########

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []


print (f"{a},{b},{c}")
print (a+b+c)

