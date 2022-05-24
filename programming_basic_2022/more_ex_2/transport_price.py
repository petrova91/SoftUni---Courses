count_km = int(input())
word = input()
if 20 <= count_km < 100:
    bus_price_km = 0.09
    total_price_bus = count_km * bus_price_km
    print(f'{total_price_bus:.2f}')
elif count_km >= 100:
    train_price = 0.06
    total_price_train = count_km * train_price
    print(f'{total_price_train:.2f}')
else:
    start_tax = 0.70
    if word == 'day':
        day_tax = 0.79
        total_price_taxi = start_tax + count_km * day_tax
        print(f'{total_price_taxi:.2f}')
    elif word == 'night':
        night_tax = 0.90
        total_price_taxi = start_tax + count_km * night_tax
        print(f'{total_price_taxi:.2f}')
