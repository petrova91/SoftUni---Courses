budget = float(input())
season = input()
type_class = 'Economy class'
type_car = 'Cabrio'
price = 0
if budget <= 100:
    type_class
    if season == 'Summer':
        type_car
        price = budget * 0.35
    elif season == 'Winter':
        type_car = 'Jeep'
        price = budget * 0.65
elif budget <= 500:
    type_class = 'Compact class'
    if season == 'Summer':
        type_car
        price = budget * 0.45
    elif season == 'Winter':
        type_car = 'Jeep'
        price = budget * 0.80
elif budget > 500:
    type_class = 'Luxury class'
    if season == 'Summer' or season == 'Winter':
        type_car = 'Jeep'
        price = budget * 0.90
print(f'{type_class}')
print(f'{type_car} - {price:.2f}')

