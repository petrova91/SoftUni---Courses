count_month = int(input())
water = 20
internet = 15
others = 0
bill_electricity = 0
total_bills = 0
other_bill = 0
for current_month in range(count_month):
    electricity = float(input())
    bill_electricity += electricity
    others = (electricity + water + internet) + (electricity + water + internet) * 0.2
    other_bill += others
    total_bill_for_month = electricity + water + internet + others
    total_bills += total_bill_for_month
bill_water = water * count_month
bill_internet = internet * count_month
average = total_bills / count_month
print(f'Electricity: {bill_electricity:.2f} lv')
print(f'Water: {bill_water:.2f} lv')
print(f'Internet: {bill_internet:.2f} lv')
print(f'Other: {other_bill:.2f} lv')
print(f'Average: {average:.2f} lv')
