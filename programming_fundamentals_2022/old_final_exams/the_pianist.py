def add_piece(pieces_dict, data_line):
    command_name, piece_name, composer_name, piece_key = data_line.split("|")
    if piece_name not in pieces_dict:
        pieces_dict[piece_name] = {"composer": composer_name, "key": piece_key}
        print(f"{piece_name} by {composer_name} in {piece_key} added to the collection!")
    else:
        print(f"{piece_name} is already in the collection!")
    return pieces_dict


def remove_piece(piece_dict, data_line):
    command_name, piece_name = data_line.split("|")
    if piece_name in piece_dict:
        piece_dict.pop(piece_name)
        print(f"Successfully removed {piece_name}!")
    else:
        print(f"Invalid operation! {piece_name} does not exist in the collection.")
    return piece_dict


def change_key(piece_dict, data_line):
    command_name, piece_name, new_key = data_line.split("|")
    if piece_name in piece_dict:
        piece_dict[piece_name]["key"] = new_key
        print(f"Changed the key of {piece_name} to {new_key}!")
    else:
        print(f"Invalid operation! {piece_name} does not exist in the collection.")
    return piece_dict


count_pieces = int(input())
pieces = {}
for _ in range(count_pieces):
    data = input()
    piece, composer, key = data.split("|")
    pieces[piece] = {"composer": composer, "key": key}
command = input()
while not command == "Stop":
    if "Add" in command:
        pieces = add_piece(pieces, command)
    elif "Remove" in command:
        pieces = remove_piece(pieces, command)
    elif "ChangeKey" in command:
        pieces = change_key(pieces, command)
    command = input()
for current_piece, values in pieces.items():
    print(f'{current_piece} -> Composer: {values["composer"]}, Key: {values["key"]}')