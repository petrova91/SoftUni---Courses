number_n = int(input())
counter_combination = 0
all_is_printed = False
for number_a in range(1, 9+1):
    for number_b in range(9, number_a-1, -1):
        for number_c in range(0, 9+1):
            for number_d in range(9, number_c-1, -1):
                number_sum = number_a + number_b + number_c + number_d
                number_uber = number_a * number_b * number_c * number_d
                if number_sum == number_uber and number_n % 10 == 5:
                    print(f'{number_a}{number_b}{number_c}{number_d}')
                    counter_combination += 1
                    all_is_printed = True
                    break
                elif number_uber // number_sum == 3 and number_n % 3 == 0:
                    print(f'{number_d}{number_c}{number_b}{number_a}')
                    counter_combination += 1
                    all_is_printed = True
                    break
            if all_is_printed:
                break
        if all_is_printed:
            break
    if all_is_printed:
        break
if counter_combination == 0:
    print('Nothing found')