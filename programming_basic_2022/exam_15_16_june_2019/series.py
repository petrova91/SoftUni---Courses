budget = float(input())
count_series = int(input())
total_price = 0
for current_series in range(count_series):
    name_series = input()
    price_series = float(input())
    if name_series == 'Thrones':
        price_series *= 0.50
    elif name_series == 'Lucifer':
        price_series *= 0.60
    elif name_series == 'Protector':
        price_series *= 0.70
    elif name_series == 'TotalDrama':
        price_series *= 0.80
    elif name_series == 'Area':
        price_series *= 0.90
    total_price += price_series
different = abs(budget - total_price)
if budget >= total_price:
    print(f'You bought all the series and left with {different:.2f} lv.')
else:
    print(f'You need {different:.2f} lv. more to buy the series!')