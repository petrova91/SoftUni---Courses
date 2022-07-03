def calculate(digit):
    even_sum = 0
    odd_sum = 0
    for element in digit:
        if int(element) % 2 == 0:
            even_sum += int(element)
        else:
            odd_sum += int(element)
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


number = input()
calculate(number)