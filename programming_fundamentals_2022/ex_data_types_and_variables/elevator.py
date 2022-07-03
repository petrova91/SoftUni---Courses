import math

number_people = int(input())
capacity_elevator = int(input())
courses = 0
full_elevator = math.floor(number_people / capacity_elevator)
courses += full_elevator
number_people -= courses * capacity_elevator
if 0 < number_people <= capacity_elevator:
    courses += 1
print(courses)



