budget = float(input())
name_product = input()
count_bought_products = 0
total_bill = 0
money_are_finish = False
while name_product != 'Stop':
    count_bought_products += 1
    price_product = float(input())
    if count_bought_products % 3 == 0:
        price_product *= 0.5
    if price_product > budget:
        budget -= price_product
        money_are_finish = True
        break
    total_bill += price_product
    budget -= price_product
    name_product = input()
if money_are_finish:
    print("You don't have enough money!")
    print(f'You need {abs(budget):.2f} leva!')
else:
    print(f'You bought {count_bought_products} products for {total_bill:.2f} leva.')