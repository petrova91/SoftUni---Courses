name_airline = input()
count_ticket_adult = int(input())
count_ticket_kid = int(input())
price_adult_ticket = float(input())
tax_service = float(input())
price_kid_ticket = price_adult_ticket * 0.3
total_price_adult_ticket = price_adult_ticket + tax_service
total_price_kid_ticket = price_kid_ticket + tax_service
total_price_ticket = (count_ticket_adult * total_price_adult_ticket) + \
                     (count_ticket_kid * total_price_kid_ticket)
win_airline = total_price_ticket * 0.2
print(f'The profit of your agency from {name_airline} tickets is {win_airline:.2f} lv.')