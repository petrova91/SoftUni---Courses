year_tax = int(input())
price_basketball_sneakers = year_tax * 0.60
price_basketball_clothes = price_basketball_sneakers * 0.80
price_ball = price_basketball_clothes / 4
price_accessories = price_ball / 5
total_price = year_tax + price_basketball_sneakers + price_basketball_clothes + price_ball + price_accessories
print(f'{total_price:.2f}')