season = input()
kilometres_for_month = float(input())
price = 0
if kilometres_for_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price = 0.75
    elif season == 'Summer':
        price = 0.90
    elif season == 'Winter':
        price = 1.05
elif kilometres_for_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price = 0.95
    elif season == 'Summer':
        price = 1.10
    elif season == 'Winter':
        price = 1.25
elif kilometres_for_month <= 20000:
    price = 1.45
total_win = (kilometres_for_month * price) * 4
total_win *= 0.90
print(f'{total_win:.2f}')
