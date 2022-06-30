employees_happiness = input().split()
improvement_factor = int(input())
happy_count = 0
happiness = list(map(int, employees_happiness))
multiply_happiness = [x*3 for x in happiness]
average_happiness = sum(multiply_happiness) / len(multiply_happiness)
for element in multiply_happiness:
    if element >= average_happiness:
        happy_count += 1
if happy_count >= len(happiness) / 2:
    print(f'Score: {happy_count}/{len(happiness)}. Employees are happy!')
else:
    print(f'Score: {happy_count}/{len(happiness)}. Employees are not happy!')
