start_count_eggs = int(input())
command = input()
count_sold_eggs = 0
eggs_are_finish = False
while command != 'Close':
    count_eggs = int(input())
    if command == 'Buy':
        if count_eggs > start_count_eggs:
            eggs_are_finish = True
            break
        else:
            count_sold_eggs += count_eggs
            start_count_eggs -= count_eggs
    elif command == 'Fill':
        start_count_eggs += count_eggs
    command = input()
if eggs_are_finish:
    print('Not enough eggs in store!')
    print(f'You can buy only {start_count_eggs}.')
else:
    print('Store is closed!')
    print(f'{count_sold_eggs} eggs sold.')