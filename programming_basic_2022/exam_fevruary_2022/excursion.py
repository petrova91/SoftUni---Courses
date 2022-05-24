count_people = int(input())
count_overnights = int(input())
count_travel_cards = int(input())
count_museum_tickets = int(input())
price_overnights = 20
price_travel_cards = 1.60
price_museum_tickets = 6
other_costs = 0.25
total_bill = ((price_overnights * count_overnights) +
             (price_travel_cards * count_travel_cards) +
             (price_museum_tickets * count_museum_tickets)) * count_people
total_bill += total_bill * other_costs
print(f'{total_bill:.2f}')