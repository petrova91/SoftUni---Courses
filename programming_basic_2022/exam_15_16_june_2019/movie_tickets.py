number_a1 = int(input())
number_a2 = int(input())
number_n = int(input())
end_first_symbol = number_a2 - 1
end_second_symbol = number_n - 1
end_third_symbol = int((number_n / 2) - 1)
for first_symbol in range(number_a1, end_first_symbol+1):
    for second_symbol in range(1, end_second_symbol+1):
        for third_symbol in range(1, end_third_symbol+1):
            fourth_symbol = first_symbol
            sum = second_symbol + third_symbol + fourth_symbol
            if first_symbol % 2 == 1 and sum % 2 == 1:
                print(f'{chr(first_symbol)}-{second_symbol}{third_symbol}{fourth_symbol}')

