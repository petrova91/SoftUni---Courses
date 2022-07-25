contact = input()
phonebook = {}
while '-' in contact:
    contact_line = contact.split('-')
    name = contact_line[0]
    number = contact_line[1]
    phonebook[name] = number
    contact = input()
count_search_items = int(contact)
for element in range(count_search_items):
    searched_name = input()
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
