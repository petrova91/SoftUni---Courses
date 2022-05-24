size_eggs = input()
colour_of_eggs = input()
count_batch = int(input())   # брой партиди
price_batch = 0
if size_eggs == 'Large':
    if colour_of_eggs == 'Red':
        price_batch = 16
    elif colour_of_eggs == 'Green':
        price_batch = 12
    elif colour_of_eggs == 'Yellow':
        price_batch = 9
elif size_eggs == 'Medium':
    if colour_of_eggs == 'Red':
        price_batch = 13
    elif colour_of_eggs == 'Green':
        price_batch = 9
    elif colour_of_eggs == 'Yellow':
        price_batch = 7
elif size_eggs == 'Small':
    if colour_of_eggs == 'Red':
        price_batch = 9
    elif colour_of_eggs == 'Green':
        price_batch = 8
    elif colour_of_eggs == 'Yellow':
        price_batch = 5
total_win = count_batch * price_batch
costs = total_win * 0.35
total_win -= costs
print(f'{total_win:.2f} leva.')