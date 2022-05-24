total_places = int(input())
total_fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0
for current_fan in range(1, total_fans + 1):
    sector = input()
    if sector == 'A':
        fans_a += 1
    elif sector == 'B':
        fans_b += 1
    elif sector == 'V':
        fans_v += 1
    elif sector == 'G':
        fans_g += 1
percent_fans_a = (fans_a / total_fans) * 100
percent_fans_b = (fans_b / total_fans) * 100
percent_fans_v = (fans_v / total_fans) * 100
percent_fans_g = (fans_g / total_fans) * 100
percent_total_fans = (total_fans / total_places) * 100
print(f'{percent_fans_a:.2f}%')
print(f'{percent_fans_b:.2f}%')
print(f'{percent_fans_v:.2f}%')
print(f'{percent_fans_g:.2f}%')
print(f'{percent_total_fans:.2f}%')