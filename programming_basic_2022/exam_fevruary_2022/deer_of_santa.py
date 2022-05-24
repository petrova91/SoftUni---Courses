import math

missing_days = int(input())
left_foot = int(input())
first_deer_foot_for_day = float(input())
second_deer_foot_for_day = float(input())
third_deer_foot_for_day = float(input())
total_count_foot_for_first_deer = missing_days * first_deer_foot_for_day
total_count_foot_for_second_deer = missing_days * second_deer_foot_for_day
total_count_foot_for_third_deer = missing_days * third_deer_foot_for_day
needed_foot = total_count_foot_for_first_deer + total_count_foot_for_second_deer + total_count_foot_for_third_deer
different = abs(left_foot - needed_foot)
if needed_foot <= left_foot:
    print(f'{math.floor(different)} kilos of food left.')
else:
    print(f'{math.ceil(different)} more kilos of food are needed.')