price_strawberries = float(input())
count_bananas = float(input())
count_oranges = float(input())
count_raspberries = float(input())
count_strawberries = float(input())
price_raspberries = price_strawberries / 2
price_oranges = price_raspberries * 0.60
price_bananas = price_raspberries * 0.20
total_bill = (price_strawberries * count_strawberries) + \
             (price_bananas * count_bananas) + (price_oranges * count_oranges) + \
             (price_raspberries * count_raspberries)
print(f'{total_bill:.2f}')