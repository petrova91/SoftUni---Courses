number = int(input())
end_char = 97 + number
for first_letter in range(97, end_char):
    for second_letter in range(97, end_char):
        for third_letter in range(97, end_char):
            print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}')
