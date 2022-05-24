season = input()   # Winter, Spring, Summer
kind_of_group = input()   # boys, girls, mixed
count_students = int(input())
count_overnight = int(input())
price_overnight = 0
kind_of_sport = ''
if season == 'Winter':
    if kind_of_group == 'boys':
        price_overnight = 9.60
        kind_of_sport = 'Judo'
    elif kind_of_group == 'girls':
        price_overnight = 9.60
        kind_of_sport = 'Gymnastics'
    elif kind_of_group == 'mixed':
        price_overnight = 10
        kind_of_sport = 'Ski'
elif season == 'Spring':
    if kind_of_group == 'boys':
        price_overnight = 7.20
        kind_of_sport = 'Tennis'
    elif kind_of_group == 'girls':
        price_overnight = 7.20
        kind_of_sport = 'Athletics'
    elif kind_of_group == 'mixed':
        price_overnight = 9.50
        kind_of_sport = 'Cycling'
elif season == 'Summer':
    if kind_of_group == 'boys':
        price_overnight = 15
        kind_of_sport = 'Football'
    elif kind_of_group == 'girls':
        price_overnight = 15
        kind_of_sport = 'Volleyball'
    elif kind_of_group == 'mixed':
        price_overnight = 20
        kind_of_sport = 'Swimming'
total_price = (price_overnight * count_overnight) * count_students
if count_students >= 50:
    total_price *= 0.50
elif 20 <= count_students < 50:
    total_price *= 0.85
elif 10<= count_students <20:
    total_price *= 0.95
print(f'{kind_of_sport} {total_price:.2f} lv.')