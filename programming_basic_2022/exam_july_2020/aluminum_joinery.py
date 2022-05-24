count_windows = int(input())
size_windows = input()
way_to_getting = input()
price_window = 0
price_delivery = 60
is_valid_order = True
if count_windows <= 10:
    is_valid_order = False
if size_windows == "90X130":
    price_window = 110
    if 30 < count_windows <= 60:
        price_window *= 0.95
    elif count_windows > 60:
        price_window *= 0.92
elif size_windows == "100X150":
    price_window = 140
    if 40 < count_windows <= 80:
        price_window *= 0.94
    elif count_windows > 80:
        price_window *= 0.90
elif size_windows == "130X180":
    price_window = 190
    if 20 < count_windows <= 50:
        price_window *= 0.93
    elif count_windows > 50:
        price_window *= 0.88
elif size_windows == "200X300":
    price_window = 250
    if 25 < count_windows <= 50:
        price_window *= 0.91
    elif count_windows > 50:
        price_window *= 0.86
total_price = price_window * count_windows
if way_to_getting == 'With delivery':
    total_price += price_delivery
if count_windows > 99:
    total_price *= 0.96
if is_valid_order:
    print(f'{total_price:.2f} BGN')
else:
    print('Invalid order')
