minutes_walk = int(input())
count_walk = int(input())
count_accepted_calories = int(input())
calories_burned_per_minute = 5
total_minutes_walk = minutes_walk * count_walk
total_burned_calories = total_minutes_walk * calories_burned_per_minute
needed_calories_burned = count_accepted_calories * 0.5
if total_burned_calories >= needed_calories_burned:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.')
