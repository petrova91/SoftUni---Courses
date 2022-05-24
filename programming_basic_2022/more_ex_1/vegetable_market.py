price_vegetable_lv = float(input())
price_fruit_lv = float(input())
total_kg_vegetable = int(input())
total_kg_fruit = int(input())
#1e=1.94lv
total_payout_lv = price_vegetable_lv * total_kg_vegetable + price_fruit_lv * total_kg_fruit
total_payout_e = total_payout_lv / 1.94
print(f'{total_payout_e:.2f}')