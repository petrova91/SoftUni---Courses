budget = float(input())
gender = input()
age = int(input())
sport = input()
price_card = 0
if gender == 'm':
    if sport == 'Gym':
        price_card = 42
    elif sport == 'Boxing':
        price_card = 41
    elif sport == 'Yoga':
        price_card = 45
    elif sport == 'Zumba':
        price_card = 34
    elif sport == 'Dances':
        price_card = 51
    elif sport == 'Pilates':
        price_card = 39
elif gender == 'f':
    if sport == 'Gym':
        price_card = 35
    elif sport == 'Boxing':
        price_card = 37
    elif sport == 'Yoga':
        price_card = 42
    elif sport == 'Zumba':
        price_card = 31
    elif sport == 'Dances':
        price_card = 53
    elif sport == 'Pilates':
        price_card = 37
if age <= 19:
    price_card *= 0.80
if price_card <= budget:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    different = abs(budget - price_card)
    print(f"You don't have enough money! You need ${different:.2f} more.")