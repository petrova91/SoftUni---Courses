items_with_price = input().split('|')
budget = float(input())
start_budget = budget
new_price = []
price_ticket = 150
for element in items_with_price:
    current_item = element.split('->')
    type_item = current_item[0]
    price = float(current_item[1])
    if budget >= price:
        if type_item == 'Clothes' and price <= 50.00:
            budget -= price
            increase_price = price * 1.4
            new_price.append(increase_price)
        elif type_item == 'Shoes' and price <= 35.00:
            budget -= price
            increase_price = price * 1.4
            new_price.append(increase_price)
        elif type_item == 'Accessories' and price <= 20.50:
            budget -= price
            increase_price = price * 1.4
            new_price.append(increase_price)
new_budget = budget + sum(new_price)
profit = new_budget - start_budget
for i in range(len(new_price)):
    print(f'{new_price[i]:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if new_budget >= price_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')