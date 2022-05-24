count_cats = int(input())
small_cats = 0
big_cats = 0
huge_cats = 0
eaten_food = 0
price_food = 12.45
for current_cat in range(count_cats):
    food = float(input())
    if 100 <= food < 200:
        small_cats += 1
    elif 200 <= food < 300:
        big_cats += 1
    elif 300 <= food < 400:
        huge_cats += 1
    eaten_food += food
total_price_food = (eaten_food / 1000) * price_food
print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {total_price_food:.2f} lv.")
