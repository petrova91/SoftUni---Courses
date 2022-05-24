town = input()
sale = float(input())
is_not_valid = False
percent = 0
if town != 'Sofia' and town != 'Plovdiv' and town != 'Varna' or sale < 0:
    is_not_valid = True
elif town == 'Sofia':
    if sale >= 0 and sale <= 500:
        percent = 0.05
    elif sale <= 1000:
        percent = 0.07
    elif sale <= 10000:
        percent = 0.08
    elif sale > 10000:
        percent = 0.12
elif town == 'Plovdiv':
    if sale >= 0 and sale <= 500:
        percent = 0.055
    elif sale <= 1000:
        percent = 0.08
    elif sale <= 10000:
        percent = 0.12
    elif sale > 10000:
        percent = 0.145
elif town == 'Varna':
    if sale >= 0 and sale <= 500:
        percent = 0.045
    elif sale <= 1000:
        percent = 0.075
    elif sale <= 10000:
        percent = 0.10
    elif sale > 10000:
        percent = 0.13
if is_not_valid == True:
    print('error')
elif is_not_valid == False:
    commission = percent * sale
    print(f'{commission:.2f}')
