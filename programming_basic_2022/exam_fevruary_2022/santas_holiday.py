vacation_days = int(input())
kind_room = input()
score = input()
nights = vacation_days - 1
price_for_night = 0
if kind_room == 'room for one person':
    price_for_night = 18
elif kind_room == 'apartment':
    price_for_night = 25
elif kind_room == 'president apartment':
    price_for_night = 35
total_price = nights * price_for_night
if kind_room == 'apartment':
    if vacation_days < 10:
        total_price *= 0.70
    elif vacation_days <= 15:
        total_price *= 0.65
    else:
        total_price *= 0.50
elif kind_room == 'president apartment':
    if vacation_days < 10:
        total_price *= 0.90
    elif vacation_days <= 15:
        total_price *= 0.85
    else:
        total_price *= 0.80
if score == 'positive':
    total_price *= 1.25
elif score == 'negative':
    total_price *= 0.90
print(f'{total_price:.2f}')