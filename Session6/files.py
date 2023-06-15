import csv

# with open(file="dogs_are_awsome.csv", mode="r", encoding="utf-8") as my_file:
#     csv_reader = csv.reader(my_file)
#     for row in csv_reader:
#         print(row)

# with open(file="hello.csv", mode="w") as my_file:
#     csv_writer = csv.writer(my_file)
#     csv_writer.writerow(["Hello"])

# population=[]
# with open(file="2016_pilbara.csv") as csv_file:
#     csv_reader=csv.reader(csv_file)
#     for line in csv_reader:
#         population.append(line)

# print(population)



# with open(file="population.csv") as csv_file:
#     csv_writer= csv.writer(csv_file, delimiter="-")

# for age_group in population:
#     #print(f"{age_group[0]* {age_group[1]}}")
#     age_group, frequency = age_group
#     print(age_group)
#     print(type(age_group))
#     print(frequency)
#     print(type(frequency))

##################EXERCISES#####################

#################Q1#####################
    # Write a program that reads in colours_20_simple.csv and print each
    #  line of the colourdata one by one as a string. Use spaces to 
    # separate the columns insead of commas.

with open("/Users/andrearivera/Desktop/SheCodes/python_shecodes/Session6/colours_20_simple.csv") as colours:
 
    for colour in colours:
    # Each row in the data gets converted into a list.
        print(colour)

##################Q2####################
#Write a program that reads in colours_20_simple.csv and outputs the colour 
#data inorder English, Hex then RGB, like so:

with open("/Users/andrearivera/Desktop/SheCodes/python_shecodes/Session6/colours_20_simple.csv", encoding="utf-8") as colours:
 
    reader = csv.reader(colours)
   # loop time!
    for colour in reader:
    # Each row in the data gets converted into a list.
        print(f"{colour[2]}, Hex: {colour[1]}, RGB: {colour[0]}")

#################Q3####################
#Write a program that takes a csv file describing colours, 
# and outputs the number oftimes each of the following colours 
# appears in the English Name.

with open("/Users/andrearivera/Desktop/SheCodes/python_shecodes/Session6/colours_20_simple.csv", encoding="utf-8") as colours:
 
    reader = csv.reader(colours)
    red_counter=0
    green_counter =0
    blue_counter=0
    yellow_counter=0
   # loop time!
    for colour in reader:
    # Each row in the data gets converted into a list.
        separated_colour= colour[2].split(" ")
        #print(separated_colour)
        for color in separated_colour:
            color=color.lower()
            if color=="red":
                red_counter = red_counter+1
            if color=="green":
                green_counter = green_counter+1
            if color=="blue":
                blue_counter = blue_counter+1
            if color=="yellow":
                yellow_counter = yellow_counter+1
          
    print(f"Red: {red_counter}")
    print(f"Green: {green_counter}")
    print(f"Blue: {blue_counter}")
    print(f"Yellow: {yellow_counter}")
        
       


####    Q4
#galaxies.csv contains data about 82 different galaxies and their 
# velocities (km/sec).Using this data, print a string showing the galaxy 
# with the slowest velocity, and another showing the galaxy with the highest 
# velocity

with open("/Users/andrearivera/Desktop/SheCodes/python_shecodes/Session6/galaxies.csv", encoding="utf-8") as galaxies:
 
    reader = csv.reader(galaxies)
    velocity=[]

    for galaxy in reader:
        number =int(galaxy[1])
        velocity.append(number)
    print(velocity)
    print(f"Galaxy {velocity.index(min(velocity))+1} has the min velocity of {min(velocity)}")
    print(f"Galaxy {velocity.index(max(velocity))+1} has the max velocity of {max(velocity)}")
  