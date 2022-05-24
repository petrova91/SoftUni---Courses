number_of_orders = int(input())
total_price = 0
for current_order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules = int(input())
    if 0.01 > price_per_capsule or price_per_capsule > 100.00:
        continue
    elif 1 > days or days > 31:
        continue
    elif 1 > needed_capsules or needed_capsules > 2000:
        continue
    else:
        price_order = price_per_capsule * needed_capsules * days
        total_price += price_order
        print(f'The price for the coffee is: ${price_order:.2f}')
print(f'Total: ${total_price:.2f}')