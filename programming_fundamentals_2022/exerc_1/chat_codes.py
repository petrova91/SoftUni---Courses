number_sent_messages = int(input())
for _ in range(number_sent_messages):
    number = int(input())
    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    elif number != 88 and number != 86 and number < 88:
        print('GREAT!')
    elif number > 88:
        print('Bye.')