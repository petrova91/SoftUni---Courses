gift_list = input().split()
command = input()
while command != 'No Money':
    command = command.split()
    name_command = command[0]
    gift_name = command[1]
    if name_command == 'OutOfStock':
        for index, current_gift in enumerate(gift_list):
            if current_gift == gift_name:
                gift_list[index] = 'None'
    elif name_command == 'Required':
        index_replace_gift = int(command[2])
        if 0 <= index_replace_gift < len(gift_list):
            gift_list[index_replace_gift] = gift_name
    elif name_command == 'JustInCase':
        gift_list[-1] = gift_name
    command = input()
for i in range(len(gift_list)):
    if gift_list[i] == 'None':
        continue
    print(f'{gift_list[i]}', end=' ')

