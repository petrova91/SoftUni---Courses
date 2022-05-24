budget_film = float(input())
count_statist = int(input())
price_clothes = float(input())
decor = budget_film * 0.10
total_price_clothes = count_statist * price_clothes
if count_statist > 150:
    total_price_clothes *= 0.90
total_price = decor + total_price_clothes
different = abs(budget_film - total_price)
if total_price > budget_film:
    print('Not enough money!')
    print(f'Wingard needs {different:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {different:.2f} leva left.')