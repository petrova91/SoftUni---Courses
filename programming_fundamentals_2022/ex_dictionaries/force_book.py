def split_command(current_command):
    side = ''
    user = ''
    if '|' in current_command:
        command_line = current_command.split(' | ')
        side = command_line[0]
        user = command_line[1]
    elif '->' in current_command:
        command_line = current_command.split(' -> ')
        side = command_line[1]
        user = command_line[0]
    return side, user


def chek_user(force_dict, user):
    user_is_existing = False
    for users in force_dict.values():
        if user in users:
            user_is_existing = True
            break
    return user_is_existing


def add_side_and_user(force_dict, side, user):
    if side not in force_dict:
        force_dict[side] = [user]
    else:
        force_dict[side].append(user)
    return force_dict


def remove_user(force_dict, user, side):
    for key, values in force_dict.items():
        if user in values:
            force_dict[key].remove(user)
            break
    return force_dict


def print_data(force_dict):
    for side, users in force_dict.items():
        if len(users) > 0:
            print(f'Side: {side}, Members: {len(users)}')
            for user in users:
                print(f'! {user}')


command = input()
force_book = {}
while command != 'Lumpawaroo':
    force_side, force_user = split_command(command)
    user_is_added = chek_user(force_book, force_user)
    if '|' in command:
        if not user_is_added:
            force_book = add_side_and_user(force_book, force_side, force_user)
    elif '->' in command:
        if user_is_added:
            remove_user(force_book, force_user, force_side)
        force_book = add_side_and_user(force_book, force_side, force_user)
        print(f'{force_user} joins the {force_side} side!')
    command = input()
print_data(force_book)