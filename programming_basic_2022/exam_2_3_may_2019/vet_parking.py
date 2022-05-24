count_days = int(input())
count_hours = int(input())
parking_tax = 0
total_sum = 0
for current_day in range(1, count_days+1):
    sum_for_day = 0
    for current_hour in range(1, count_hours+1):
        if current_day % 2 == 0 and current_hour % 2 == 1:
            parking_tax = 2.50
            sum_for_day += parking_tax
            total_sum += parking_tax
        elif current_day % 2 == 1 and current_hour % 2 == 0:
            parking_tax = 1.25
            sum_for_day += parking_tax
            total_sum += parking_tax
        else:
            parking_tax = 1
            sum_for_day += parking_tax
            total_sum += parking_tax
    print(f'Day: {current_day} - {sum_for_day:.2f} leva')
print(f'Total: {total_sum:.2f} leva')