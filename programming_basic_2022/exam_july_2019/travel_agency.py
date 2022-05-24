town_name = input()
type_packet = input()
vip_discount = input()
rest_day = int(input())
price_for_day = 0
if rest_day < 1:
    print('Days must be positive number!')
if(town_name != 'Bansko' and town_name != 'Borovets' and town_name != 'Varna' and town_name !='Burgas') or \
        (type_packet != 'noEquipment' and type_packet != 'withEquipment' and type_packet != 'noBreakfast' and \
         type_packet != 'withBreakfast'):
    print('Invalid input!')
else:
    if town_name == 'Bansko' or town_name == 'Borovets':
        if type_packet == 'withEquipment':
            if vip_discount == 'no':
                price_for_day = 100
            else:
                price_for_day = 100 * 0.9
        elif type_packet == 'noEquipment':
             if vip_discount == 'no':
                price_for_day = 80
             else:
                price_for_day = 80 * 0.95
    elif town_name == 'Varna' or town_name == 'Burgas':
        if type_packet == 'withBreakfast':
            if vip_discount == 'no':
                price_for_day = 130
            else:
                price_for_day = 130 * 0.88
        elif type_packet == 'noBreakfast':
            if vip_discount == 'no':
                price_for_day = 100
            else:
                price_for_day = 100 * 0.93
    if 0 < rest_day <= 7:
        total_bill = price_for_day * rest_day
        print(f'The price is {total_bill:.2f}lv! Have a nice time!')
    elif rest_day > 7:
        total_bill = price_for_day * (rest_day - 1)
        print(f'The price is {total_bill:.2f}lv! Have a nice time!')
