price_vegetables = float(input())
price_fruits = float(input())
quantity_vegetables = int(input())
quantity_fruits = int(input())
earning_vegetables = price_vegetables * quantity_vegetables
earning_fruits = price_fruits * quantity_fruits
total_earning_euro = (earning_fruits + earning_vegetables) / 1.94
print(f'{total_earning_euro}')