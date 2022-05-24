fuel = input()
litres = float(input())
club_card = input()
price_gasoline = 2.22
price_diesel = 2.33
price_gas = 0.93
discount_gasoline = 0.18
discount_diesel = 0.12
discount_gas = 0.08
total_bill = 0
if club_card == 'Yes':
    if fuel == 'Gasoline':
        total_bill = litres * (price_gasoline - discount_gasoline)
    elif fuel == 'Diesel':
        total_bill = litres * (price_diesel - discount_diesel)
    elif fuel == 'Gas':
        total_bill = litres * (price_gas - discount_gas)
elif club_card == 'No':
    if fuel == 'Gasoline':
        total_bill = litres * price_gasoline
    elif fuel == 'Diesel':
        total_bill = litres * price_diesel
    elif fuel == 'Gas':
        total_bill = litres * price_gas
if litres >= 20 and litres <= 25:
    total_bill *= 0.92
elif litres > 25:
    total_bill *= 0.90
print(f'{total_bill:.2f} lv.')