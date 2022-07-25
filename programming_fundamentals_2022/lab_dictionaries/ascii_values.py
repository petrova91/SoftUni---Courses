list_letters = input().split(', ')
letters_dict = {key: ord(key) for key in list_letters}
print(letters_dict)