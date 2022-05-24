film_name = input()
menu_for_film = input()
count_tickets = int(input())
price = 0
if film_name == 'John Wick':
    if menu_for_film == 'Drink':
        price = 12
    elif menu_for_film == 'Popcorn':
        price = 15
    elif menu_for_film == 'Menu':
        price = 19
elif film_name == 'Star Wars':
    if menu_for_film == 'Drink':
        price = 18
    elif menu_for_film == 'Popcorn':
        price = 25
    elif menu_for_film == 'Menu':
        price = 30
elif film_name == 'Jumanji':
    if menu_for_film == 'Drink':
        price = 9
    elif menu_for_film == 'Popcorn':
        price = 11
    elif menu_for_film == 'Menu':
        price = 14
total_price = price * count_tickets
if film_name == 'Star Wars' and count_tickets >= 4:
    total_price *= 0.70
if film_name == 'Jumanji' and count_tickets == 2:
    total_price *= 0.85
print(f'Your bill is {total_price:.2f} leva.')