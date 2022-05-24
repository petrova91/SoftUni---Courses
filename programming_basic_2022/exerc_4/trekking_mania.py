count_group = int(input())
group_musala = 0
group_monblan = 0
group_kilimandjaro = 0
group_k2 = 0
group_everest = 0
total_people = 0
for current_group in range(count_group):
    count_people = int(input())
    total_people += count_people
    if count_people <= 5:
        group_musala += count_people
    elif count_people <= 12:
        group_monblan += count_people
    elif count_people <= 25:
        group_kilimandjaro += count_people
    elif count_people <= 40:
        group_k2 += count_people
    else:
        group_everest += count_people
percent_people_musala = (group_musala / total_people) * 100
percent_people_monblan = (group_monblan / total_people) * 100
percent_people_kilimandjaro = (group_kilimandjaro / total_people) * 100
percent_people_k2 = (group_k2 / total_people) * 100
percent_people_everest = (group_everest / total_people) * 100
print(f'{percent_people_musala:.2f}%')
print(f'{percent_people_monblan:.2f}%')
print(f'{percent_people_kilimandjaro:.2f}%')
print(f'{percent_people_k2:.2f}%')
print(f'{percent_people_everest:.2f}%')
