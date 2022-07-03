sequence_of_numbers = input().split()
some_string = input()
some_string_list = list(map(str, some_string))
word = []
for element in sequence_of_numbers:
    sum_of_digit = 0
    sum_digit_list = []
    for i in range(len(element)):
        sum_digit_list.append(int(element[i]))
    sum_of_digit = sum(sum_digit_list)
    if sum_of_digit > len(some_string_list):
        letter_index = sum_of_digit - len(some_string_list)
        word.append(some_string_list[letter_index])
        some_string_list.pop(letter_index)
    elif sum_of_digit <= len(some_string_list):
        letter_index = sum_of_digit
        word.append(some_string_list[letter_index])
        some_string_list.pop(letter_index)
print(''.join(word))