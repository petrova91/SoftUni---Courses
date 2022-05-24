destination = input()
while destination != 'End':
    money_for_trip = float(input())
    saved_money = 0
    while saved_money < money_for_trip:
        money = float(input())
        saved_money += money
    print(f'Going to {destination}!')
    destination = input()