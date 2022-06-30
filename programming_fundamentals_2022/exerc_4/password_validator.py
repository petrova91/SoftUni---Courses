def check_valid(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        is_valid = False
        print('Password must be between 6 and 10 characters')
    if not password.isalnum():
        is_valid = False
        print('Password must consist only of letters and digits')
    count_digits = 0
    for element in password:
        if element.isdigit():
            count_digits += 1
    if count_digits < 2:
        is_valid = False
        print('Password must have at least 2 digits')
    return is_valid

some_password = input()
if check_valid(some_password):
    print('Password is valid')
