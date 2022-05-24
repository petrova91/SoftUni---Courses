count_clients = int(input())
price_basket = 1.50
price_wreath = 3.80
price_chocolate_bunny = 7
total_price = 0
for current_client in range(count_clients):
    purchase = input()   # покупка
    count_purchase = 0
    total_price_for_current_client = 0
    while purchase != 'Finish':
        if purchase == 'basket':
            count_purchase += 1
            total_price_for_current_client += price_basket
        elif purchase == 'wreath':
            count_purchase += 1
            total_price_for_current_client += price_wreath
        elif purchase == 'chocolate bunny':
            count_purchase += 1
            total_price_for_current_client += price_chocolate_bunny
        purchase = input()
    if count_purchase % 2 == 0:
        total_price_for_current_client *= 0.80
    total_price += total_price_for_current_client
    print(f'You purchased {count_purchase} items for {total_price_for_current_client:.2f} leva.')
average_bill = total_price / count_clients
print(f'Average bill per client is: {average_bill:.2f} leva.')