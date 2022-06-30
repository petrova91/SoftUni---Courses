def collect(items, new_item):
    if new_item not in items:
        items.append(new_item)


def drop(items, old_item):
    if old_item in items:
        items.remove(old_item)


def combine(items, group_items):
    command_line = group_items.split(':')
    old_item = command_line[0]
    new_item = command_line[1]
    if old_item in items:
        old_item_index = items.index(old_item)
        items.insert(old_item_index+1, new_item)


def renew(items, old_items):
    if old_items in items:
        items.remove(old_items)
        items.append(old_items)


list_with_items = input().split(', ')
command = input().split(' - ')
while 'Craft!' not in command:
    command_name = command[0]
    item = command[1]
    if command_name == 'Collect':
        collect(list_with_items, item)
    elif command_name == 'Drop':
        drop(list_with_items, item)
    elif command_name == 'Combine Items':
        combine(list_with_items, item)
    elif command_name == 'Renew':
        renew(list_with_items, item)
    command = input().split(' - ')
print(', '.join(list_with_items))