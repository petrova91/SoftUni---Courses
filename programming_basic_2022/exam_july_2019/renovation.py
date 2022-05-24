import math

height = int(input())
width = int(input())
percent_without_paint = int(input())
total_area = math.ceil((height * width) * 4)
area_without_paint = total_area * (percent_without_paint / 100)
total_area -= area_without_paint
count_paint = total_area
paint_litres = input()
pesho_is_tired = True
while paint_litres != 'Tired!':
    paint_litres = int(paint_litres)
    total_area -= paint_litres
    count_paint -= paint_litres
    if total_area <= 0:
        pesho_is_tired = False
        break
    paint_litres = input()
if pesho_is_tired:
    print(f'{math.ceil(total_area)} quadratic m left.')
else:
    if count_paint == 0:
        print(f'All walls are painted! Great job, Pesho!')
    else:
        print(f'All walls are painted and you have {math.ceil(abs(count_paint))} l paint left!')