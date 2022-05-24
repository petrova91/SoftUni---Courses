wanted_win = float(input())
total_win = 0
wanted_sum_is_reach = True
while total_win < wanted_win:
    drink_name = input()
    if drink_name == 'Party!':
        wanted_sum_is_reach = False
        break
    else:
        price_drink = len(drink_name)
        count_drink = int(input())
        total_current_price = price_drink * count_drink
        if total_current_price % 2 == 1:
            total_current_price *= 0.75
        total_win += total_current_price
if wanted_sum_is_reach:
    print('Target acquired.')
else:
    different = wanted_win - total_win
    print(f'We need {different:.2f} leva more.')
print(f'Club income - {total_win:.2f} leva.')