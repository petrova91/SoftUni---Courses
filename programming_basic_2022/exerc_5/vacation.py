money_for_trip = float(input())
pocked_money = float(input())   # налични пари
left_days = 0
spend_counter = 0
go_to_trip = True
while pocked_money < money_for_trip:
    left_days += 1
    action = input()
    daily_money = float(input())
    if action == 'spend':
        pocked_money -= daily_money
        spend_counter += 1
        if pocked_money <= 0:
            pocked_money = 0
        if spend_counter == 5:
            go_to_trip = False
            break
    elif action == 'save':
        pocked_money += daily_money
        spend_counter = 0
if go_to_trip:
    print(f'You saved the money for {left_days} days.')
else:
    print("You can't save the money.")
    print(f'{left_days}')