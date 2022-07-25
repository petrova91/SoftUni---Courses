products = input().split()
products_dict = {}
for index in range(0, len(products), 2):
    food = products[index]
    quantities = int(products[index+1])
    products_dict[food] = quantities
searched_product = input().split()
for product in searched_product:
    if product in products_dict:
        print(f'We have {products_dict[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")