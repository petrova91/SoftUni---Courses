number_lines = int(input())
sum = 0
for current_number in range(number_lines):
    letter = input()
    sum += ord(letter)
print(f'The sum equals: {sum}')