import math

count_people = int(input())
enter_tax = float(input())
price_sunbed = float(input())
price_umbrella = float(input())
total_enter_tax = count_people * enter_tax
count_umbrella = math.ceil(count_people / 2)
total_sum_umbrella = count_umbrella * price_umbrella
count_sunbed = math.ceil(count_people * 0.75)
total_sum_sunbed = count_sunbed * price_sunbed
total_sum = total_enter_tax + total_sum_umbrella + total_sum_sunbed
print(f'{total_sum:.2f} lv.')