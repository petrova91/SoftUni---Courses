film_name = input()
kind_of_hall = input()
count_tickets = int(input())
price_tickets = 0
if kind_of_hall == 'normal':
    if film_name == 'A Star Is Born':
        price_tickets = 7.50
    elif film_name == 'Bohemian Rhapsody':
        price_tickets = 7.35
    elif film_name == 'Green Book':
        price_tickets = 8.15
    elif film_name == 'The Favourite':
        price_tickets = 8.75
elif kind_of_hall == 'luxury':
    if film_name == 'A Star Is Born':
        price_tickets = 10.50
    elif film_name == 'Bohemian Rhapsody':
        price_tickets = 9.45
    elif film_name == 'Green Book':
        price_tickets = 10.25
    elif film_name == 'The Favourite':
        price_tickets = 11.55
elif kind_of_hall == 'ultra luxury':
    if film_name == 'A Star Is Born':
        price_tickets = 13.50
    elif film_name == 'Bohemian Rhapsody':
        price_tickets = 12.75
    elif film_name == 'Green Book':
        price_tickets = 13.25
    elif film_name == 'The Favourite':
        price_tickets = 13.95
total_price = price_tickets * count_tickets
print(f'{film_name} -> {total_price:.2f} lv.')