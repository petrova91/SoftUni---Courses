count_bottle_detergent = int(input())
volume_detergent = 750
detergent_plate = 5
detergent_pan = 15
total_count_detergent = count_bottle_detergent * volume_detergent
count_clean_plate = 0
count_clean_pan = 0
counter_washing = 0
enough_detergent = True
command = input()
while command != 'End':
    counter_washing += 1
    count_utensils = int(command)  # количество съдове
    if counter_washing % 3 == 0:
        count_clean_pan += count_utensils
        consumption_detergent = count_utensils * detergent_pan    # разход веро
        total_count_detergent -= consumption_detergent
    else:
        count_clean_plate += count_utensils
        consumption_detergent = count_utensils * detergent_plate
        total_count_detergent -= consumption_detergent
    if total_count_detergent < 0:
        enough_detergent = False
        break
    command = input()
if enough_detergent:
    print('Detergent was enough!')
    print(f'{count_clean_plate} dishes and {count_clean_pan} pots were washed.')
    print(f'Leftover detergent {total_count_detergent} ml.')

else:
    print(f'Not enough detergent, {abs(total_count_detergent)} ml. more necessary!')



