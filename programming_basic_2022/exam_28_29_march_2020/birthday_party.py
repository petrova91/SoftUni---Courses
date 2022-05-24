rent_hall = float(input())
price_cake = rent_hall * 0.20
price_drinks = price_cake * 0.55
price_animator = rent_hall / 3
total_price = rent_hall + price_cake + price_drinks + price_animator
print(f'{total_price:.1f}')