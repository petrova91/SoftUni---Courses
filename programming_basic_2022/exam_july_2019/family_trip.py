budget = float(input())
count_overnights = int(input())
price_overnight = float(input())
percent_more_cost = int(input())
if count_overnights > 7:
    price_overnight *= 0.95
total_price = count_overnights * price_overnight
more_cost = budget * (percent_more_cost / 100)
total_price += more_cost
different = abs(budget - total_price)
if budget >= total_price:
    print(f'Ivanovi will be left with {different:.2f} leva after vacation.')
else:
    print(f'{different:.2f} leva needed.')