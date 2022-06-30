def is_palindrome(numbers):
    forward_number = numbers
    backward_number = numbers[::-1]
    if forward_number == backward_number:
        return True
    return False


sequence_of_numbers = input().split(', ')
for current_number in sequence_of_numbers:
    print(is_palindrome(current_number))