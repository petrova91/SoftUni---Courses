sequence_of_number = input().split(', ')
num_as_integer = list(map(int, sequence_of_number))
border = 10
while len(num_as_integer) > 0:
    num_list = [element for element in num_as_integer if element <= border]
    print(f"Group of {border}'s: {num_list}")
    border += 10
    for number in num_list:
        num_as_integer.remove(number)