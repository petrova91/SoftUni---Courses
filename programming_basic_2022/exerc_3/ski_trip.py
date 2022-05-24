day_for_rest = int(input())
room = input()
score = input()
overnight = day_for_rest - 1
price_overnight = 0
if room == 'room for one person':
    price_overnight = 18
elif room == 'apartment':
    price_overnight = 25
elif room == 'president apartment':
    price_overnight = 35
total_price = price_overnight * overnight
if room == 'apartment':
    if overnight < 10:
        total_price *= 0.70
    elif 10 <= overnight <= 15:
        total_price *= 0.65
    else:
        total_price *= 0.50
elif room == 'president apartment':
    if overnight < 10:
        total_price *= 0.90
    elif 10 <= overnight <= 15:
        total_price *= 0.85
    else:
        total_price *= 0.80
if score == 'positive':
    total_price *= 1.25
else:
    total_price *= 0.90
print(f'{total_price:.2f}')