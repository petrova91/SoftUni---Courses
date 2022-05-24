count_painted_eggs = int(input())
count_red_eggs = 0
count_orange_eggs = 0
count_blue_eggs = 0
count_green_eggs = 0
max_count_painted_eggs = 0
paint_of_max_count_eggs = ''
for current_egg in range(count_painted_eggs):
    paint = input()
    if paint == 'red':
        count_red_eggs += 1
        if count_red_eggs > max_count_painted_eggs:
            max_count_painted_eggs = count_red_eggs
            paint_of_max_count_eggs = paint
    elif paint == 'orange':
        count_orange_eggs += 1
        if count_orange_eggs > max_count_painted_eggs:
            max_count_painted_eggs = count_orange_eggs
            paint_of_max_count_eggs = paint
    elif paint == 'blue':
        count_blue_eggs += 1
        if count_blue_eggs > max_count_painted_eggs:
            max_count_painted_eggs = count_blue_eggs
            paint_of_max_count_eggs = paint
    elif paint == 'green':
        count_green_eggs += 1
        if count_green_eggs > max_count_painted_eggs:
            max_count_painted_eggs = count_green_eggs
            paint_of_max_count_eggs = paint
print(f'Red eggs: {count_red_eggs}')
print(f'Orange eggs: {count_orange_eggs}')
print(f'Blue eggs: {count_blue_eggs}')
print(f'Green eggs: {count_green_eggs}')
print(f'Max eggs: {max_count_painted_eggs} -> {paint_of_max_count_eggs}')
