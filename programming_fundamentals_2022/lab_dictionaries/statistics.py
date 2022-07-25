command = input()
products_in_stock = {}
while command != 'statistics':
    groceries = command.split(': ')
    product = groceries[0]
    quantities = int(groceries[1])
    if product not in products_in_stock:
        products_in_stock[product] = quantities
    else:
        products_in_stock[product] += quantities
    command = input()
print('Products in stock:')
for key, value in products_in_stock.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(products_in_stock)}')
print(f'Total Quantity: {sum(products_in_stock.values())}')