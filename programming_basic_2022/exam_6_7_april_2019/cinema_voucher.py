voucher_money = int(input())
product = input()
count_tickets = 0
other_products = 0
price = 0
while product != 'End':
    length_symbol = len(product)
    if length_symbol > 7:
        price = ord(product[0]) + ord(product[1])
        if price <= voucher_money:
            voucher_money -= price
            count_tickets += 1
        else:
            break
    elif length_symbol <= 7:
        price = ord(product[0])
        if price <= voucher_money:
            voucher_money -= price
            other_products += 1
        else:
            break
    product = input()
print(f'{count_tickets}')
print(f'{other_products}')