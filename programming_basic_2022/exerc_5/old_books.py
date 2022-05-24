favorite_book = input()
counter_book = 0
current_book = input()
finding_favorite_book = False
while current_book != 'No More Books':
    if current_book == favorite_book:
        finding_favorite_book = True
        break
    counter_book += 1
    current_book = input()
if finding_favorite_book:
    print(f'You checked {counter_book} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {counter_book} books.')