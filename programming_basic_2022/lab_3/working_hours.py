hour = int(input())
day = input()
is_valid = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or \
    day == 'Friday' or day == 'Saturday'
if is_valid == True and hour >= 10 and hour <= 18:
    print('open')
else:
    print('closed')