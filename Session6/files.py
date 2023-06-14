import csv

with open(file="dogs_are_awsome.csv", mode="r", encoding="utf-8") as my_file:
    csv_reader = csv.reader(my_file)
    for row in csv_reader:
        print(row)

with open(file="hello.csv", mode="w") as my_file:
    csv_writer = csv.writer(my_file)
    csv_writer.writerow(["Hello"])

population=[]
with open(file="2016_pilbara.csv") as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in csv_reader:
        population.append(line)

print(population)



with open(file="population.csv") as csv_file:
    csv_writer= csv.writer(csv_file, delimiter="-")

for age_group in population:
    #print(f"{age_group[0]* {age_group[1]}}")
    age_group, frequency = age_group
    print(age_group)
    print(type(age_group))
    print(frequency)
    print(type(frequency))