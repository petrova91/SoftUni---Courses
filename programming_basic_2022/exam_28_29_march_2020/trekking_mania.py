count_groups = int(input())
count_total_climbers = 0
climb_musala = 0
climb_monblan = 0
climb_kilimandjaro = 0
climb_k2 = 0
climb_everest = 0
for current_group in range(count_groups):
    count_climbers = int(input())
    if count_climbers <= 5:
        climb_musala += count_climbers
        count_total_climbers += count_climbers
    elif 6 <= count_climbers <= 12:
        climb_monblan += count_climbers
        count_total_climbers += count_climbers
    elif 13 <= count_climbers <= 25:
        climb_kilimandjaro += count_climbers
        count_total_climbers += count_climbers
    elif 26 <= count_climbers <= 40:
        climb_k2 += count_climbers
        count_total_climbers += count_climbers
    elif count_climbers > 40:
        climb_everest += count_climbers
        count_total_climbers += count_climbers
percent_musala = (climb_musala / count_total_climbers) * 100
percent_monblan = (climb_monblan / count_total_climbers) * 100
percent_kilimandjaro = (climb_kilimandjaro / count_total_climbers) * 100
percent_k2 = (climb_k2 / count_total_climbers) * 100
percent_everest = (climb_everest / count_total_climbers) * 100
print(f'{percent_musala:.2f}%')
print(f'{percent_monblan:.2f}%')
print(f'{percent_kilimandjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')
