capacity_rack = float(input())   # капацитет на багажник
count_suitcases = 0
no_more_spaces = False
volume_suitcase = input()
while volume_suitcase != 'End':
    volume_suitcase = float(volume_suitcase)
    count_suitcases += 1
    if count_suitcases % 3 == 0:
        volume_suitcase += volume_suitcase * 0.10
    if volume_suitcase <= capacity_rack:
        capacity_rack -= volume_suitcase
    else:
        no_more_spaces = True
        count_suitcases -= 1
        break
    volume_suitcase = input()
if no_more_spaces:
    print('No more space!')
else:
    print('Congratulations! All suitcases are loaded!')
print(f'Statistic: {count_suitcases} suitcases loaded.')