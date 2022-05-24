count_hrisantema = int(input())
count_roses = int(input())
count_tupils = int(input())
season = input()
holiday = input()
price_hrisantema = 0
price_roses = 0
price_tulips = 0
if season == 'Spring' or season == 'Summer':
    price_hrisantema = 2
    price_roses = 4.10
    price_tulips = 2.50
elif season == 'Autumn' or season == 'Winter':
    price_hrisantema = 3.75
    price_roses = 4.50
    price_tulips = 4.15
total_sum = count_hrisantema * price_hrisantema + count_roses * price_roses + \
    count_tupils * price_tulips
if holiday == 'Y':
    total_sum *= 1.15
if count_tupils > 7 and season == 'Spring':
    total_sum *= 0.95
if count_roses >= 10 and season == 'Winter':
    total_sum *= 0.9
if count_hrisantema + count_roses + count_tupils > 20:
    total_sum *= 0.80
total_sum += 2
print(f'{total_sum:.2f}')