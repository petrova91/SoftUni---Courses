month = input()
count_roosting = int(input())
price_studio = 0
price_apartment = 0
if month == 'May' or month == 'October':
    price_studio = 50
    price_apartment = 65
elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_apartment = 68.70
elif month == 'July' or month == 'August':
    price_studio = 76
    price_apartment = 77
if 7 < count_roosting < 14 and (month == 'May' or month == 'October'):
    price_studio *= 0.95
elif count_roosting > 14:
    price_apartment *= 0.90
    if month == 'May' or month == 'October':
        price_studio *= 0.70
    elif month == 'June' or month == 'September':
        price_studio *= 0.80
total_price_apartment = count_roosting * price_apartment
total_price_studio = count_roosting * price_studio
print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')
