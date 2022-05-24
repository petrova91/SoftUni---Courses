count_coins_1_lev = int(input())
count_coins_2_leva = int(input())
count_banknote_5_leva = int(input())
sum = int(input())
for counter_1_lev in range(0, count_coins_1_lev+1):
    for counter_2_leva in range(0, count_coins_2_leva+1):
        for counter_5_leva in range(0, count_banknote_5_leva+1):
            if counter_1_lev * 1 + counter_2_leva * 2 + counter_5_leva * 5 == sum:
                print(f'{counter_1_lev} * 1 lv. + {counter_2_leva} * 2 lv. + {counter_5_leva} * 5 lv. = {sum} lv.')