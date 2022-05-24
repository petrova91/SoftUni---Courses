count_guests = int(input())
price_cover_for_one_guest = float(input())
budget = float(input())
if 10 <= count_guests <= 15:
    price_cover_for_one_guest *= 0.85
elif 15 < count_guests <= 20:
    price_cover_for_one_guest *= 0.80
elif count_guests > 20:
    price_cover_for_one_guest *= 0.75
price_cake = budget * 0.10
total_price = (count_guests * price_cover_for_one_guest) + price_cake
different = abs(budget - total_price)
if budget >= total_price:
    print(f'It is party time! {different:.2f} leva left.')
else:
    print(f'No party! {different:.2f} leva needed.')