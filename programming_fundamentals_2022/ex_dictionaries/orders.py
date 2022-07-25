product_information = input().split()
product_dict = dict()
while 'buy' not in product_information:
    name_product = product_information[0]
    price = float(product_information[1])
    quantity = int(product_information[2])
    if name_product not in product_dict:
        product_dict[name_product] = {}
        product_dict[name_product]['price'] = 0
        product_dict[name_product]['quantity'] = 0
    product_dict[name_product]['price'] = price
    product_dict[name_product]['quantity'] += quantity
    product_information = input().split()
for product in product_dict:
    product_price = product_dict[product]['price']
    product_quantity = product_dict[product]['quantity']
    total_price = product_price * product_quantity
    print(f'{product} -> {total_price:.2f}')