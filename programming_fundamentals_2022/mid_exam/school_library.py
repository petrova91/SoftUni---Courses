books_shelf = input().split('&')
command = input()
while 'Done' not in command:
    command_line = command.split(' | ')
    command_name = command_line[0]
    if command_name == 'Add Book':
        name = command_line[1]
        if name not in books_shelf:
            books_shelf.insert(0, name)
    elif command_name == 'Take Book':
        name = command_line[1]
        if name in books_shelf:
            books_shelf.remove(name)
    elif command_name == 'Swap Books':
        first_book = command_line[1]
        second_book = command_line[2]
        if first_book in books_shelf and second_book in books_shelf:
            index_first_book = books_shelf.index(first_book)
            index_second_book = books_shelf.index(second_book)
            books_shelf[index_first_book], books_shelf[index_second_book] = books_shelf[index_second_book], books_shelf[index_first_book]
    elif command_name == 'Insert Book':
        name = command_line[1]
        if name not in books_shelf:
            books_shelf.append(name)
    elif command_name == 'Check Book':
        index_book = int(command_line[1])
        if 0 <= index_book < len(books_shelf):
            print(books_shelf[index_book])
    command = input()
print(', '.join(books_shelf))