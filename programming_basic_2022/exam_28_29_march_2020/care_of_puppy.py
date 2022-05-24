purchased_food_kg = int(input())
purchased_food_gr = purchased_food_kg * 1000
count_eaten_food = 0
eaten_food = input()
while eaten_food != 'Adopted':
    eaten_food = int(eaten_food)
    count_eaten_food += eaten_food
    eaten_food = input()
different = abs(purchased_food_gr - count_eaten_food)
if count_eaten_food <= purchased_food_gr:
    print(f'Food is enough! Leftovers: {different} grams.')
else:
    print(f'Food is not enough. You need {different} grams more.')