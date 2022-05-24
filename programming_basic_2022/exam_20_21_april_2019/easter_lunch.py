count_kozunaci = int(input())
count_bark_for_eggs = int(input())
kilograms_of_cookies = int(input())
price_kozunak = 3.20
price_bark_for_eggs = 4.35
price_cookies = 5.40
price_paint_for_one_egg = 0.15
price_paint_for_all_eggs = (count_bark_for_eggs * 12) * price_paint_for_one_egg
total_price = (count_kozunaci * price_kozunak) + (count_bark_for_eggs * price_bark_for_eggs) + \
              (kilograms_of_cookies * price_cookies) + price_paint_for_all_eggs
print(f'{total_price:.2f}')