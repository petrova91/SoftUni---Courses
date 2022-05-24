price_trip = float(input())
count_puzzle = int(input())
count_doll = int(input())
count_bear = int(input())
count_minions = int(input())
count_truck = int(input())
price_puzzle = 2.60
price_doll = 3
price_bear = 4.10
price_minions = 8.20
price_truck = 2
count_toys = count_puzzle + count_doll + count_bear + count_minions + count_truck
total_price = count_puzzle * price_puzzle + \
    count_doll * price_doll + \
    count_bear * price_bear + \
    count_minions * price_minions + \
    count_truck * price_truck
if count_toys >= 50:
    total_price *= 0.75
rent = total_price * 0.1
total_price_without_rent = total_price - rent
difference = abs(total_price_without_rent - price_trip)
if price_trip <= total_price_without_rent:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')
