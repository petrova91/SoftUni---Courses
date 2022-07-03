def find_result(some_data_type):
    result = None
    if some_data_type == 'int':
        number = int(input())
        result = number * 2
    elif some_data_type == 'real':
        number = float(input())
        result = f'{(number * 1.5):.2f}'
    elif some_data_type == 'string':
        some_string = input()
        result = '$'+some_string+'$'
    return result


data_type = input()
print(find_result(data_type))