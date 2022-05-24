count_loads = int(input())  # брой товари
total_weight = 0
total_price = 0
weight_microbus = 0
weight_truck = 0
weight_train = 0
for current_loads in range(1, count_loads + 1):
    weight_loads = int(input())  # тонаж на товара
    if weight_loads <= 3:
        price_for_ton_microbus = 200
        price_microbus = weight_loads * price_for_ton_microbus
        total_price += price_microbus
        weight_microbus += weight_loads
    elif weight_loads <= 11:
        price_for_ton_truck = 175
        price_truck = weight_loads * price_for_ton_truck
        total_price += price_truck
        weight_truck += weight_loads
    elif weight_loads >= 12:
        price_for_ton_train = 120
        price_train = weight_loads * price_for_ton_train
        total_price += price_train
        weight_train += weight_loads
    total_weight += weight_loads
middle_price = total_price / total_weight
percent_weight_microbus = (weight_microbus / total_weight) * 100
percent_weight_truck = (weight_truck / total_weight) * 100
percent_weight_train = (weight_train / total_weight) * 100
print(f'{middle_price:.2f}')
print(f'{percent_weight_microbus:.2f}%')
print(f'{percent_weight_truck:.2f}%')
print(f'{percent_weight_train:.2f}%')
