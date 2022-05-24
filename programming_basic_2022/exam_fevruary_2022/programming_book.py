price_page = float(input())
price_cover = float(input())
percent_discount = int(input())
designer_price = float(input())
percent_team = int(input())
count_pages = 899
count_covers = 2
total_bill = (count_pages * price_page) + (count_covers * price_cover)
total_bill -= total_bill * (percent_discount / 100)
total_bill += designer_price
total_bill -= total_bill * (percent_team / 100)
print(f'Avtonom should pay {total_bill:.2f} BGN.')