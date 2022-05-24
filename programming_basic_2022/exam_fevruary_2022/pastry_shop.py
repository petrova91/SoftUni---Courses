dessert = input()
count_dessert = int(input())
day_of_month = int(input())
price_dessert = 0
if day_of_month <= 15:
    if dessert == 'Cake':
        price_dessert = 24
    elif dessert == 'Souffle':
        price_dessert = 6.66
    elif dessert == 'Baklava':
        price_dessert = 12.60
elif day_of_month > 15:
    if dessert == 'Cake':
        price_dessert = 28.70
    elif dessert == 'Souffle':
        price_dessert = 9.80
    elif dessert == 'Baklava':
        price_dessert = 16.98
total_bill = count_dessert * price_dessert
if day_of_month <= 22:
    if 100 < total_bill <= 200:
        total_bill *= 0.85
    elif total_bill > 200:
        total_bill *= 0.75
if day_of_month <= 15:
    total_bill *= 0.90
print(f'{total_bill:.2f}')