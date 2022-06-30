first_stings = input().split(', ')
second_strings = input().split(', ')
string_list = []
for element in first_stings:
    for word in second_strings:
        if element in word and element not in string_list:
            string_list.append(element)
            break
print(string_list)