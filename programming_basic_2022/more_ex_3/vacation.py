budget = float(input())
season = input()
location = 'Alaska'   # Morocco
place_to_stay = 'Hotel'   # Hut or Camp
price = 0
if budget <= 1000:
    place_to_stay = 'Camp'
    if season == 'Summer':
        location
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif budget <= 3000:
    place_to_stay = 'Hut'
    if season == 'Summer':
        location
        price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.60
elif budget > 3000:
    place_to_stay
    if season == 'Summer':
        location
        price = budget * 0.90
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.90
print(f'{location} - {place_to_stay} - {price:.2f}')
