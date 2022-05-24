import math

count_magnolia = int(input())
count_hyacinth = int(input())   #зюмбюл
count_rose = int(input())
count_cactus = int(input())
price_present = float(input())
price_magnolia = 3.25
price_hyacinth = 4
price_rose = 3.50
price_cactus = 8
sum_order = count_magnolia * price_magnolia + \
    count_hyacinth * price_hyacinth + \
    count_rose * price_rose + \
    count_cactus * price_cactus
tax = sum_order * 0.05
payout = sum_order - tax
remaining_money = abs(payout - price_present)
if payout >= price_present:
    print(f'She is left with {math.floor(remaining_money)} leva.')
else:
    print(f'She will have to borrow {math.ceil(remaining_money)} leva.')