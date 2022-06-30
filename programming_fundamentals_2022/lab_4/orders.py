def solve_price(name_product, count_product):
    total_price = None
    if name_product == 'coffee':
        total_price = count_product * coffee_price
    elif name_product == 'coke':
        total_price = count_product * coke_price
    elif name_product == 'water':
        total_price = count_product * water_price
    elif name_product == 'snacks':
        total_price = count_product * snacks_price
    return f'{total_price:.2f}'


product = input()
quantity = int(input())
coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00
print(solve_price(product, quantity))