budget = int(input())
season = input()
count_fisherman = int(input())
rent_boat = 0
if season == 'Spring':
    rent_boat = 3000
elif season == 'Summer' or season == 'Autumn':
    rent_boat = 4200
elif season == 'Winter':
    rent_boat = 2600
if count_fisherman <= 6:
    rent_boat *= 0.90
elif count_fisherman <= 11:
    rent_boat *= 0.85
elif count_fisherman >= 12:
    rent_boat *= 0.75
if season != 'Autumn' and count_fisherman % 2 == 0:
    rent_boat *= 0.95
different = abs(rent_boat - budget)
if budget >= rent_boat:
    print(f'Yes! You have {different:.2f} leva left.')
else:
    print(f'Not enough money! You need {different:.2f} leva.')