number_lines = int(input())
count_opening_brackets = 0
count_closing_brackets = 0
is_balanced = True
last_string = ''
for i in range(number_lines):
    random_string = input()
    if random_string == last_string:
        is_balanced = False
    last_string = random_string
    if random_string == '(':
        count_opening_brackets += 1
    elif random_string == ')':
        count_closing_brackets += 1
if count_opening_brackets == count_closing_brackets and is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')