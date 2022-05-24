count_naylon = int(input())
count_paint = int(input())
count_diluent = int(input())
hours_working = int(input())
price_naylon = 1.50
price_paint = 14.50
price_diluent = 5.00
price_bags = 0.40
total_price_naylon = (count_naylon + 2) * price_naylon
total_price_paint = (count_paint + (count_paint * 0.10)) * price_paint
total_price_diluent = count_diluent * price_diluent
total_price = total_price_naylon + total_price_paint + total_price_diluent + price_bags
total_hours_working = hours_working * (total_price * 0.30)
total_price = total_price + total_hours_working
print(total_price)




# Сумата, която се заплаща на майсторите за 1 час работа, е равна на 30% от сбора на всички разходи за материали.
