age_lili = int(input())
price_laundry = float(input())
toy_price = int(input())
count_toy = 0
birthday_money = 0
total_money = 0
for count_spin in range(1, age_lili +1):
    if count_spin % 2 != 0:
        count_toy += 1
    else:
        birthday_money += 10
        total_money += birthday_money - 1
total_money = total_money + (count_toy * toy_price)
difference = abs(total_money - price_laundry)
if total_money >= price_laundry:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
