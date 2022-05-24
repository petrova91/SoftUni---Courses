budget = float(input())
litres_fuel = float(input())
day_of_week = input()
price_fuel = 2.10
price_guide = 100
total_price = price_guide + (litres_fuel * price_fuel)
if day_of_week == 'Saturday':
    total_price *= 0.90
elif day_of_week == 'Sunday':
    total_price *= 0.80
different = abs(budget - total_price)
if budget >= total_price:
    print(f'Safari time! Money left: {different:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {different:.2f} lv.')