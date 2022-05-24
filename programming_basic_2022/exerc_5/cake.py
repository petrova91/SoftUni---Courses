width = int(input())
length = int(input())
cake_size = width * length
command = input()
cake_is_not_over = True
while command != 'STOP':
    count_pieces = int(command)
    cake_size -= count_pieces
    if cake_size < 0:
        cake_is_not_over = False
        break
    command = input()
if cake_is_not_over:
    print(f'{cake_size} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_size)} pieces more.')