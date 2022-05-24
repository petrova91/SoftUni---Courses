budget = float(input())
category = input()
count_people = int(input())
price_tickets = 0
money_for_transport = 0
if category == 'VIP':
    price_tickets = 499.99
elif category == 'Normal':
    price_tickets = 249.99
if 1 <= count_people <= 4:
    money_for_transport = budget * 0.75
elif count_people <= 9:
    money_for_transport = budget * 0.60
elif count_people <= 24:
    money_for_transport = budget * 0.50
elif count_people <= 49:
    money_for_transport = budget * 0.40
else:
    money_for_transport = budget * 0.25
left_money = budget - money_for_transport
money_for_tickets = count_people * price_tickets
different = abs(left_money - money_for_tickets)
if left_money >= money_for_tickets:
    print(f'Yes! You have {different:.2f} leva left.')
else:
    print(f'Not enough money! You need {different:.2f} leva.')