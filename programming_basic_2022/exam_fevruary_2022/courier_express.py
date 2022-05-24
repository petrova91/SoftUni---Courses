weight = float(input())
type_delivery = input()
distance = int(input())
price_for_kilometre = 0
delivery_is_standard = True
total_costly = 0
if type_delivery == 'standard' or type_delivery == 'express':
    if weight < 1:
        price_for_kilometre = 0.03
    elif weight < 10:
        price_for_kilometre = 0.05
    elif weight < 40:
        price_for_kilometre = 0.10
    elif weight < 90:
        price_for_kilometre = 0.15
    elif weight < 150:
        price_for_kilometre = 0.20
total_price = distance * price_for_kilometre
if type_delivery == 'express':
    delivery_is_standard = False
    if weight < 1:
        costly_for_weight = price_for_kilometre * 0.80
        costly_for_distance = costly_for_weight * weight
        total_costly = costly_for_distance * distance
    elif weight < 10:
        costly_for_weight = price_for_kilometre * 0.40
        costly_for_distance = costly_for_weight * weight
        total_costly = costly_for_distance * distance
    elif weight < 40:
        costly_for_weight = price_for_kilometre * 0.05
        costly_for_distance = costly_for_weight * weight
        total_costly = costly_for_distance * distance
    elif weight < 90:
        costly_for_weight = price_for_kilometre * 0.02
        costly_for_distance = costly_for_weight * weight
        total_costly = costly_for_distance * distance
    elif weight < 150:
        costly_for_weight = price_for_kilometre * 0.01
        costly_for_distance = costly_for_weight * weight
        total_costly = costly_for_distance * distance
total_price_express = total_costly + total_price
if delivery_is_standard:
    print(f'The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_price:.2f} lv.')
else:
    print(f'The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_price_express:.2f} lv.')