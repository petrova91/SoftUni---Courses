budget = float(input())
count_statistician = int(input())
price_dress = float(input())
decor = budget * 0.1
if count_statistician > 150:
    price_dress *= 0.9
total_sum = decor + (count_statistician * price_dress)
different = abs(budget - total_sum)
if total_sum > budget:
    print('Not enough money!')
    print(f'Wingard needs {different:.2f} leva more.')
elif total_sum <= budget:
    print('Action!')
    print(f'Wingard starts filming with {different:.2f} leva left.')
