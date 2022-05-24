price_flour = float(input())
kilograms_flours = float(input())
kilograms_sugar = float(input())
count_bark_for_eggs = int(input())
packets_of_yeast = int(input())
price_sugar = price_flour * 0.75
price_bark_for_eggs = price_flour * 1.10
price_yeast = price_sugar * 0.20
total_price = (price_flour * kilograms_flours) + (price_sugar * kilograms_sugar) + \
              (price_bark_for_eggs * count_bark_for_eggs) + (packets_of_yeast * price_yeast)
print(f'{total_price:.2f}')