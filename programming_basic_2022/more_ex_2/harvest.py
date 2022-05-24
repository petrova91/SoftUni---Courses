import math

total_area = int(input())
grape_for_meter = float(input())
needed_wine = int(input())
count_workers = int(input())
total_yield_grape = total_area * grape_for_meter
yield_grape_kg = total_yield_grape * 0.4
yield_grape_l = yield_grape_kg / 2.5
if yield_grape_l < needed_wine:
    missing_litres = math.floor(needed_wine - yield_grape_l)
    print(f'It will be a tough winter! More {missing_litres} liters wine needed.')
elif yield_grape_l >= needed_wine:
    down = math.floor(yield_grape_l)
    print(f'Good harvest this year! Total wine: {down} liters.')
    bonus_wine = math.ceil(yield_grape_l - needed_wine)
    wine_worker = math.ceil(bonus_wine / count_workers)
    print(f'{bonus_wine} liters left -> {wine_worker} liters per person.')


