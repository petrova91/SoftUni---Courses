some_string = input()
list_capitals_letter = []
for index, char in enumerate(some_string):
    if char.isupper():
        list_capitals_letter.append(index)
print(list_capitals_letter)