budget = float(input())
count_videocard = int(input())
count_cpu = int(input())
count_ram = int(input())
price_videocard = 250
cost_videocard = count_videocard * price_videocard
price_cpu = cost_videocard * 0.35
price_ram = cost_videocard * 0.1
total_bill = cost_videocard + \
    count_cpu * price_cpu + \
    count_ram * price_ram
if count_videocard > count_cpu:
    total_bill *= 0.85
different = abs(budget - total_bill)
if budget >= total_bill:
    print(f'You have {different:.2f} leva left!')
else:
    print(f'Not enough money! You need {different:.2f} leva more!')