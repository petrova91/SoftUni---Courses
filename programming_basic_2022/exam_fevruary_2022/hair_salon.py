purpose_for_day = int(input())
service = input()
win = 0
price_service = 0
target_is_not_achieve = True
while service != 'closed':
    if service == 'haircut':
        kind_service = input()
        if kind_service == 'mens':
            price_service = 15
            win += price_service
        elif kind_service == 'ladies':
            price_service = 20
            win += price_service
        elif kind_service == 'kids':
            price_service = 10
            win += price_service
    elif service == 'color':
        kind_service = input()
        if kind_service == 'touch up':
            price_service = 20
            win += price_service
        elif kind_service == 'full color':
            price_service = 30
            win += price_service
    if win >= purpose_for_day:
        target_is_not_achieve = False
        break
    service = input()
if target_is_not_achieve:
    different = purpose_for_day - win
    print(f'Target not reached! You need {different:.2f}lv. more.')
else:
    print(f'You have reached your target for the day!')
print(f'Earned money: {win:.2f}lv.')