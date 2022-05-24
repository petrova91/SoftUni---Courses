width = int(input())
length = int(input())
height = int(input())
free_place = width * length * height
free_places_is_not_over = True
command = input()
while command != 'Done':
    count_boxes = int(command)
    free_place -= count_boxes
    if free_place <= 0:
        free_places_is_not_over = False
        break
    command = input()
if free_places_is_not_over:
    print(f'{free_place} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(free_place)} Cubic meters more.')