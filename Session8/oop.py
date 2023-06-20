class Dog:
    # state/attributes

    def __init__(self, dog_name, dog_age, dog_breed, dog_weight): #dog_name = "Jett"
        self.name = dog_name
        self.age = dog_age
        self.breed = dog_breed
        self.weight = dog_weight

    #methods/behaviours 
    def eat(self): # self parameter during definition
        print("Nom nom")
        self.weight += 0.5

    def talk(self):
        print("Bark bark")

#dog1 = Dog(dog_name="Jett", dog_age=4, dog_breed="pug") # instantiate 
dog2 = Dog("Ninja", 13, "dutch-shephard", 23)
# print(dog2.weight)
dog2.eat()
# print(dog2.weight)
#print(dog2.age)
#dog1.talk() # no self argument during calling
# print(dog1)
# print(type(dog1))

class Book():

    def __init__(self, title, author, pages, current_page):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
    
    def __len__(self):
        return self.pages
    
    def bookmark_page(self):
        self.bookmark = self.current_page

    def turn_page(self):
        self.current_page += 1 
    
my_book = Book("A great book", "me", 198, 1)
print(my_book)
my_book.bookmark_page()
print(my_book.bookmark)
my_book.turn_page()
my_book.bookmark_page()
print(my_book.bookmark)

print("--------------------------------")

#####################   Q1  #############################
##Create a class to represent She Codes Students. Attributes that you may want to include
class She_codes:
    def __init__(self, student_name, student_program, student_year): 
        self.name = student_name
        self.program = student_program
        self.year = student_year

################### Q2 ##############################
##Add a __str__ method to your student class that returns a summary of the student'sinformation.
    def __str__(self):
        return f"Student: {self.name}, Program: {self.program}, Year: {self.year}"

student = She_codes("Olivia", "Plus",1956)
print(student)

##################  Q3 #############################
###Write a class that represents a rectangle shape and has a method 
# for each of the following
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.height * self.width

    def __str__(self):
        return f"Rectangle area: {self.area()}"
    
rectangle1= Rectangle(12,34)
print(rectangle1)
print(rectangle1.area())


