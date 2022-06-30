food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
guinea_weight = float(input())
something_is_over = False
food_quantity_grams = food_quantity * 1000
hay_quantity_grams = hay_quantity * 1000
cover_quantity_grams = cover_quantity * 1000
guinea_weight_grams = guinea_weight * 1000
for current_day in range(1, 31):
    food_quantity_grams -= 300
    if current_day % 2 == 0:
        hay_quantity_grams -= food_quantity_grams * 0.05
    if current_day % 3 == 0:
        cover_quantity_grams -= guinea_weight_grams / 3
    if food_quantity_grams <= 0 or hay_quantity_grams <= 0 or cover_quantity_grams <= 0:
        something_is_over = True
        break
if something_is_over:
    print('Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {(food_quantity_grams/1000):.2f}, '
          f'Hay: {(hay_quantity_grams/1000):.2f}, Cover: {(cover_quantity_grams/1000):.2f}.')