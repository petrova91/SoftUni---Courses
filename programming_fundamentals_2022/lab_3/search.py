number_lines = int(input())
word = input()
all_strings = list()
for i in range(number_lines):
    some_string = input()
    all_strings.append(some_string)
print(all_strings)
for i in range(len(all_strings)-1, -1, -1):
    element = all_strings[i]
    if word not in element:
        all_strings.remove(element)
print(all_strings)
