import math

count_guests = int(input())
budget = int(input())
price_kozunak = 4
price_egg = 0.45
count_kozunaci = count_guests / 3
count_kozunaci = math.ceil(count_kozunaci)
count_eggs = count_guests * 2
total_price = (count_kozunaci * price_kozunak) + (count_eggs * price_egg)
different = abs(budget - total_price)
if budget >= total_price:
    print(f'Lyubo bought {count_kozunaci} Easter bread and {count_eggs} eggs.')
    print(f'He has {different:.2f} lv. left.')
else:
    print("Lyubo doesn't have enough money.")
    print(f'He needs {different:.2f} lv. more.')