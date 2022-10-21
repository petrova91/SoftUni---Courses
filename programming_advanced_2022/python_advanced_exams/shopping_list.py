def shopping_list(budget, **kwargs):
    result = []
    count_products = 5
    if budget < 100:
        return "You do not have enough budget."

    for product, product_info in kwargs.items():
        price = float(product_info[0])
        quantity = int(product_info[1])
        total_price = price * quantity
        if total_price <= budget:
            budget -= total_price
            count_products -= 1
            result.append(f"You bought {product} for {total_price:.2f} leva.")
        if count_products == 0:
            break
    return '\n'.join(result)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


