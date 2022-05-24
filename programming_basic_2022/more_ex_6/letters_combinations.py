start_letter = input()
end_letter = input()
without_this_letter = input()
count_combinations = 0
for first_letter in range(ord(start_letter), ord(end_letter) + 1):
    for second_letter in range(ord(start_letter), ord(end_letter) + 1):
        for third_letter in range(ord(start_letter), ord(end_letter) + 1):
            if chr(first_letter) != without_this_letter and chr(second_letter) != without_this_letter and \
                    chr(third_letter) != without_this_letter:
                count_combinations += 1
                print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}', end=' ')
print(count_combinations)

# функцията ord() - превръща буквата в негото цифрова комбинация (от ASCII - таплица)
# функцията chr() - превъща цифровата комбинация в буква (от ASCII - таплица)