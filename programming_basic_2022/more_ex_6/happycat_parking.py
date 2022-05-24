count_days = int(input())
count_hours_for_day = int(input())
price_parking = 0
total_price = 0
for current_day in range(1, count_days+1):
    total_price_for_day = 0
    for current_hour in range(1, count_hours_for_day+1):
        if current_day % 2 == 0 and current_hour % 2 == 1:
            price_parking = 2.50
            total_price_for_day += price_parking
            total_price += price_parking
        elif current_day % 2 == 1 and current_hour % 2 == 0:
            price_parking = 1.25
            total_price_for_day += price_parking
            total_price += price_parking
        else:
            price_parking = 1
            total_price_for_day += price_parking
            total_price += price_parking
    print(f'Day: {current_day} - {total_price_for_day:.2f} leva')
print(f'Total: {total_price:.2f} leva')