number_a = int(input())
number_b = int(input())
max_count_passwords = int(input())
counter_password = 0
all_is_printed = False
for symbol_a in range(35, 56):
    for symbol_b in range(64, 97):
        for symbol_x in range(1, number_a+1):
            for symbol_y in range(1, number_b+1):
                counter_password += 1
                print(f'{chr(symbol_a)}{chr(symbol_b)}{symbol_x}{symbol_y}{chr(symbol_b)}{chr(symbol_a)}',end='|')
                symbol_a += 1
                if symbol_a > 55:
                    symbol_a = 35
                symbol_b += 1
                if symbol_b > 96:
                    symbol_b = 64
                if counter_password == max_count_passwords:
                    all_is_printed = True
                    break
                if symbol_x == number_a and symbol_y == number_b:
                    all_is_printed = True
                    break
            if all_is_printed:
                break
        if all_is_printed:
            break
    if all_is_printed:
        break

