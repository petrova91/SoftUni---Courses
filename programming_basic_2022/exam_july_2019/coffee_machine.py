hot_drinks = input()
sugar = input()
count_hot_drinks = int(input())
price = 0
if hot_drinks == 'Espresso':
    if sugar == 'Without':
        price = 0.90
    elif sugar == 'Normal':
        price = 1.00
    elif sugar == 'Extra':
        price = 1.20
elif hot_drinks == 'Cappuccino':
    if sugar == 'Without':
        price = 1.00
    elif sugar == 'Normal':
        price = 1.20
    elif sugar == 'Extra':
        price = 1.60
elif hot_drinks == 'Tea':
    if sugar == 'Without':
        price = 0.50
    elif sugar == 'Normal':
        price = 0.60
    elif sugar == 'Extra':
        price = 0.70
total_price = count_hot_drinks * price
if sugar == 'Without':
    total_price *= 0.65
if hot_drinks == 'Espresso' and count_hot_drinks >= 5:
    total_price *= 0.75
if total_price > 15:
    total_price *= 0.80
print(f'You bought {count_hot_drinks} cups of {hot_drinks} for {total_price:.2f} lv.')