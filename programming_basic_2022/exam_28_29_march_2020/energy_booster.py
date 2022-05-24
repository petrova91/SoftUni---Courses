fruit = input()
set_size = input()
count_set = int(input())
price_energy_boosters = 0
total_price = 0
if set_size == 'small':
    if fruit == 'Watermelon':
        price_energy_boosters = 56
    elif fruit == 'Mango':
        price_energy_boosters = 36.66
    elif fruit == 'Pineapple':
        price_energy_boosters = 42.10
    elif fruit == 'Raspberry':
        price_energy_boosters = 20
    total_price = (count_set * price_energy_boosters) * 2
elif set_size == 'big':
    if fruit == 'Watermelon':
        price_energy_boosters = 28.70
    elif fruit == 'Mango':
        price_energy_boosters = 19.60
    elif fruit == 'Pineapple':
        price_energy_boosters = 24.80
    elif fruit == 'Raspberry':
        price_energy_boosters = 15.20
    total_price = (count_set * price_energy_boosters) * 5
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50
print(f'{total_price:.2f} lv.')