count_excursion_sea = int(input())
count_excursion_mountain = int(input())
price_sea = 680
price_mountain = 499
win = 0
kind_excursion = input()
everything_is_sold = False
while kind_excursion != 'Stop':
    if count_excursion_sea == 0 and count_excursion_mountain == 0:
        everything_is_sold = True
        break
    if kind_excursion == 'sea':
        if count_excursion_sea > 0:
            count_excursion_sea -= 1
            win += price_sea
    else:
        if count_excursion_mountain > 0:
            count_excursion_mountain -= 1
            win += price_mountain
    kind_excursion = input()
if everything_is_sold:
    print('Good job! Everything is sold.')
print(f'Profit: {win} leva.')