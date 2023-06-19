##You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names 
#of the students and the values are their exam scores.

#Write a program that converts their scores to grades. By the end of your program, you should have a 
#new dictionary called student_grades that should contain student names for keys and their grades for values.
# The final version of the student_grades dictionary will be checked.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score=student_scores[student]
    if score >90:
        student_grades[student] = "Outstanding"
    elif score >80:
        student_grades[student] = "Exceeds Expectations"
    elif score >70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

## Nesting dictionary in a dictionary
travel_log  = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"]},
    "Germany":{"cities_visited":["Berlin", "Hamburg", "Stuttgart"],"total_visits":5}

}

##Nesting Dictionary in a List
travel_log=[
    { "country":"France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits":5
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5
    },
]


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key in dict:
    dict[key]+=1

print(dict)
dict[1] = 4
print(dict[1])
dict["c"]=[1,2,3]
print(dict)