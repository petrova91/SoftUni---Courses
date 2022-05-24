rent_hall = int(input())
price_statue = rent_hall * 0.70
price_catering = price_statue * 0.85
price_sound = price_catering * 0.50
total_price = rent_hall + price_statue + price_catering + price_sound
print(f'{total_price:.2f}')