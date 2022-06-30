shopping_list = input().split('!')
command = input()
while 'Go Shopping!' not in command:
    command = command.split()
    command_name = command[0]
    item = command[1]
    if command_name == 'Urgent':
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif command_name == 'Unnecessary':
        if item in shopping_list:
            shopping_list.remove(item)
    elif command_name == 'Correct':
        new_item = command[2]
        if item in shopping_list:
            old_item_index = shopping_list.index(item)
            shopping_list[old_item_index] = new_item
    elif command_name == 'Rearrange':
        if item in shopping_list:
            # insert on last position:
            shopping_list.insert(len(shopping_list), item)
            shopping_list.remove(item)
    command = input()
print(', '.join(shopping_list))