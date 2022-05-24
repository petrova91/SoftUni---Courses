stage_of_championship = input()
kind_of_ticket = input()
count_tickets = int(input())
photo_with_cup = input()
price_ticket = 0
if stage_of_championship == 'Quarter final':
    if kind_of_ticket == 'Standard':
        price_ticket = 55.50
    elif kind_of_ticket == 'Premium':
        price_ticket = 105.20
    elif kind_of_ticket == 'VIP':
        price_ticket = 118.90
elif stage_of_championship == 'Semi final':
    if kind_of_ticket == 'Standard':
        price_ticket = 75.88
    elif kind_of_ticket == 'Premium':
        price_ticket = 125.22
    elif kind_of_ticket == 'VIP':
        price_ticket = 300.40
elif stage_of_championship == 'Final':
    if kind_of_ticket == 'Standard':
        price_ticket = 110.10
    elif kind_of_ticket == 'Premium':
        price_ticket = 160.66
    elif kind_of_ticket == 'VIP':
        price_ticket = 400
total_price = count_tickets * price_ticket
if total_price <= 2500:
    if photo_with_cup == 'Y':
        price_photo = 40
        total_price += price_photo * count_tickets
elif 2500 < total_price <= 4000:
    total_price *= 0.90
    if photo_with_cup == 'Y':
        price_photo = 40
        total_price += price_photo * count_tickets
elif total_price > 4000:
    total_price *= 0.75
print(f'{total_price:.2f}')