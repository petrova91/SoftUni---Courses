def find_letter(start_letter, end_letter):
    list_of_letters = []
    start_letter = ord(first_letter)
    end_letter = ord(last_letter)
    for current_letter in range(start_letter+1, end_letter):
        list_of_letters.append(chr(current_letter))
    print(' '.join(list_of_letters))


first_letter = input()
last_letter = input()
find_letter(first_letter, last_letter)