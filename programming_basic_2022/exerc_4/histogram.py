count_number = int(input())
count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0
for count_spins in range(count_number):
    number = int(input())
    if number < 200:
        count_p1 += 1
    elif number <= 399:
        count_p2 += 1
    elif number <= 599:
        count_p3 += 1
    elif number <= 799:
        count_p4 += 1
    else:
        count_p5 += 1
percent_p1 = (count_p1 / count_number) * 100
percent_p2 = (count_p2 / count_number) * 100
percent_p3 = (count_p3 / count_number) * 100
percent_p4 = (count_p4 / count_number) * 100
percent_p5 = (count_p5 / count_number) * 100
print(f'{percent_p1:.2f}%')
print(f'{percent_p2:.2f}%')
print(f'{percent_p3:.2f}%')
print(f'{percent_p4:.2f}%')
print(f'{percent_p5:.2f}%')