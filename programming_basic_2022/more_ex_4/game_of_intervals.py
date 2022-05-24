rounds = int(input())
score = 0
invalid_number = 0
numbers_to_9 = 0
numbers_to_19 = 0
numbers_to_29 = 0
numbers_to_39 = 0
numbers_to_50 = 0
for current_round in range(rounds):
    number = int(input())
    if number < 0 or number > 50:
        score /= 2
        invalid_number += 1
    elif number <= 9:
        score += number * 0.2
        numbers_to_9 += 1
    elif number <= 19:
        score += number * 0.3
        numbers_to_19 += 1
    elif number <= 29:
        score += number * 0.4
        numbers_to_29 += 1
    elif number <= 39:
        score += 50
        numbers_to_39 += 1
    elif number <= 50:
        score += 100
        numbers_to_50 += 1
percent_invalid_number = (invalid_number / rounds) * 100
percent_numbers_to_9 = (numbers_to_9 / rounds) * 100
percent_numbers_to_19 = (numbers_to_19 / rounds) * 100
percent_numbers_to_29 = (numbers_to_29 / rounds) * 100
percent_numbers_to_39 = (numbers_to_39 / rounds) * 100
percent_numbers_to_50 = (numbers_to_50 / rounds) * 100
print(f'{score:.2f}')
print(f'From 0 to 9: {percent_numbers_to_9:.2f}%')
print(f'From 10 to 19: {percent_numbers_to_19:.2f}%')
print(f'From 20 to 29: {percent_numbers_to_29:.2f}%')
print(f'From 30 to 39: {percent_numbers_to_39:.2f}%')
print(f'From 40 to 50: {percent_numbers_to_50:.2f}%')
print(f'Invalid numbers: {percent_invalid_number:.2f}%')
