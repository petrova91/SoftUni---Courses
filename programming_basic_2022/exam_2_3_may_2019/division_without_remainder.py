count_number = int(input())
count_p1 = 0
count_p2 = 0
count_p3 = 0
for current_number in range(count_number):
    number = int(input())
    if number % 2 == 0:
        count_p1 += 1
    if number % 3 == 0:
        count_p2 += 1
    if number % 4 == 0:
        count_p3 += 1
percent_p1 = (count_p1 / count_number) * 100
percent_p2 = (count_p2 / count_number) * 100
percent_p3 = (count_p3 / count_number) * 100
print(f'{percent_p1:.2f}%')
print(f'{percent_p2:.2f}%')
print(f'{percent_p3:.2f}%')