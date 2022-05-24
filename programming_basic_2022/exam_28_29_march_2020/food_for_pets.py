count_days = int(input())
total_count_food = float(input())
total_eaten_biscuits = 0
eaten_food = 0
dog_food = 0
cat_food = 0
for current_day in range(1, count_days+1):
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())
    eaten_food += dog_eaten_food + cat_eaten_food
    dog_food += dog_eaten_food
    cat_food += cat_eaten_food
    if current_day % 3 == 0:
        count_eaten_food_for_current_day = dog_eaten_food + cat_eaten_food
        count_biscuits = count_eaten_food_for_current_day * 0.1
        total_eaten_biscuits += count_biscuits
percent_eaten_food = (eaten_food / total_count_food) * 100
percent_cat_eaten_food = (cat_food / eaten_food) * 100
percent_dog_eaten_food = (dog_food / eaten_food) * 100
print(f'Total eaten biscuits: {total_eaten_biscuits:.0f}gr.')
print(f'{percent_eaten_food:.2f}% of the food has been eaten.')
print(f'{percent_dog_eaten_food:.2f}% eaten from the dog.')
print(f'{percent_cat_eaten_food:.2f}% eaten from the cat.')




