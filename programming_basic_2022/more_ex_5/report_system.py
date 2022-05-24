target = int(input())
payment_cash = 0
payment_card = 0
counter_payment = 0
collect_money = 0
counter_payment_cash = 0
counter_payment_card = 0
money_are_collected = True
while collect_money < target:
    command = input()
    if command == 'End':
        money_are_collected = False
        break
    counter_payment += 1
    current_payment = int(command)
    if counter_payment % 2 == 1:
        if current_payment > 100:
            print('Error in transaction!')
            continue
        else:
            payment_cash += current_payment
            collect_money += current_payment
            counter_payment_cash += 1
            print('Product sold!')
    elif counter_payment % 2 == 0:
        if current_payment < 10:
            print('Error in transaction!')
            continue
        else:
            payment_card += current_payment
            collect_money += current_payment
            counter_payment_card += 1
            print('Product sold!')
if counter_payment_cash == 0:
    average_cash = 0
else:
    average_cash = payment_cash / counter_payment_cash
if counter_payment_card == 0:
    average_card = 0
else:
    average_card = payment_card / counter_payment_card
if money_are_collected:
    print(f'Average CS: {average_cash:.2f}')
    print(f'Average CC: {average_card:.2f}')
else:
    print('Failed to collect required money for charity.')
