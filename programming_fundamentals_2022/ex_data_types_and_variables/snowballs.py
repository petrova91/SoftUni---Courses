count_snowballs = int(input())
highest_value = 0
current_weight_snowball = 0
current_time = 0
current_quality_snowball = 0
for current_snowball in range(1, count_snowballs+1):
    weight_snowball = int(input())
    time = int(input())
    quality_snowball = int(input())
    snowball_value = (weight_snowball / time) ** quality_snowball
    if snowball_value > highest_value:
        highest_value = snowball_value
        current_weight_snowball = weight_snowball
        current_time = time
        current_quality_snowball = quality_snowball
print(f'{current_weight_snowball} : {current_time} = {highest_value:.0f} ({current_quality_snowball})')
