destination = input()
period_of_vacation = input()
count_overnights = int(input())
price_overnight = 0
if destination == 'France':
    if period_of_vacation == '21-23':
        price_overnight = 30
    elif period_of_vacation == '24-27':
        price_overnight = 35
    elif period_of_vacation == '28-31':
        price_overnight = 40
elif destination == 'Italy':
    if period_of_vacation == '21-23':
        price_overnight = 28
    elif period_of_vacation == '24-27':
        price_overnight = 32
    elif period_of_vacation == '28-31':
        price_overnight = 39
elif destination == 'Germany':
    if period_of_vacation == '21-23':
        price_overnight = 32
    elif period_of_vacation == '24-27':
        price_overnight = 37
    elif period_of_vacation == '28-31':
        price_overnight = 43
total_price = count_overnights * price_overnight
print(f'Easter trip to {destination} : {total_price:.2f} leva.')