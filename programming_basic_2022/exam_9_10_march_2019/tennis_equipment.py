import math

price_tennis_racket = float(input())
count_tennis_rackets = int(input())
count_sneakers = int(input())
price_sneakers = price_tennis_racket * (1/6)
total_price = (price_tennis_racket * count_tennis_rackets) + (price_sneakers * count_sneakers)
other_equipment = total_price * 0.2
total_price += other_equipment
paid_by_djokovic = total_price * (1/8)
paid_by_sponsors = total_price * (7/8)
print(f'Price to be paid by Djokovic {math.floor(paid_by_djokovic)}')
print(f'Price to be paid by sponsors {math.ceil(paid_by_sponsors)}')
