number_m = int(input())   # контролна стойност
count_passwords = 0
password_is_found = False
true_password = ''
current_password = ''
for number_a in range(1,10):
    for number_b in range(number_a+1,10):
        for number_c in range(1,10):
            for number_d in range(1,number_c):
                if number_a * number_b + number_c * number_d == number_m:
                    count_passwords += 1
                    current_password = f'{number_a}{number_b}{number_c}{number_d}'
                    print(current_password, end=' ')
                if count_passwords == 4:
                    true_password = current_password
                    password_is_found = True
print()
if password_is_found:
    print(f'Password: {true_password}')
else:
    print('No!')



