flower = input()
count_flower = int(input())
budget = int(input())
price_flower = 0
discount = 0
is_discount = True
if flower == 'Roses':
    price_flower = 5
    if count_flower > 80:
        discount = 0.90
    else:
        is_discount = False
elif flower == 'Dahlias':
    price_flower = 3.80
    if count_flower > 90:
        discount = 0.85
    else:
        is_discount = False
elif flower == 'Tulips':
    price_flower = 2.80
    if count_flower > 80:
        discount = 0.85
    else:
        is_discount = False
elif flower == 'Narcissus':
    price_flower = 3
    if count_flower < 120:
        discount = 1.15
    else:
        is_discount = False
elif flower == 'Gladiolus':
    price_flower = 2.50
    if count_flower < 80:
        discount = 1.20
    else:
        is_discount = False
if is_discount == True:
    total_sum = (count_flower * price_flower) * discount
else:
    total_sum = count_flower * price_flower
different = abs(budget - total_sum)
if budget >= total_sum:
    print(f'Hey, you have a great garden with {count_flower} {flower} and {different:.2f} leva left.')
else:
    print(f'Not enough money, you need {different:.2f} leva more.')

