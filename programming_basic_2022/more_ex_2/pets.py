import math

count_days = int(input())
leave_food_kg = int(input())
food_dog_kg = float(input())
food_cat_kg = float(input())
food_turtle_gr = float(input())
total_food = count_days * food_dog_kg + \
    count_days * food_cat_kg + \
    count_days * (food_turtle_gr / 1000)
different_food = abs(leave_food_kg - total_food)
if total_food <= leave_food_kg:
    print(f'{math.floor(different_food)} kilos of food left.')
else:
    print(f'{math.ceil(different_food)} more kilos of food are needed.')
