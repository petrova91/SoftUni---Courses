count_food = int(input())
command = input()
count_food *= 1000
eaten_food = 0
while command != 'Adopted':
    food = int(command)
    eaten_food += food
    command = input()
different = abs(count_food - eaten_food)
if eaten_food <= count_food:
    print(f'Food is enough! Leftovers: {different} grams.')
else:
    print(f'Food is not enough. You need {different} grams more.')