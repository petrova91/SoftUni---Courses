budget = int(input())
command = input()
while command != 'End':
    price_product = int(command)
    if price_product > budget:
        print('You went in overdraft!')
        break
    elif price_product <= budget:
        budget -= price_product
    command = input()
else:
    print('You bought everything needed.')