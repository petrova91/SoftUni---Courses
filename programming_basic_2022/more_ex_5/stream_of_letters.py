counter_c = 0
counter_o = 0
counter_n = 0
message = ''
while True:
    letter = input()
    if letter == 'End':
        break
    if letter == 'c' and counter_c == 0:
        counter_c += 1
    elif letter == 'o' and counter_o == 0:
        counter_o += 1
    elif letter == 'n' and counter_n == 0:
        counter_n += 1
    else:
        if letter.isalpha():
            message += letter
    if counter_c == 1 and counter_o == 1 and counter_n == 1:
        print(f'{message} ' , end ='')
        message = ''
        counter_c = 0
        counter_o = 0
        counter_n = 0
