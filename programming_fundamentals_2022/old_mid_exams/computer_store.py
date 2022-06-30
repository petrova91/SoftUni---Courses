command = input()
tax = 0
total_price = 0
while command != 'special' and command != 'regular':
    price = float(command)
    if price < 0:
        print('Invalid price!')
        command = input()
        continue
    tax += price * 0.2
    total_price += price
    command = input()
if total_price == 0:
    print('Invalid order!')
else:
    total_price_with_taxes = total_price + tax
    if command == 'special':
        total_price_with_taxes *= 0.90
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {tax:.2f}$')
    print('-----------')
    print(f'Total price: {total_price_with_taxes:.2f}$')
