some_text = input()
hidden_message = []
digit_list = []
symbol_list = []
take_list = []
skip_list = []
for element in some_text:
    if chr(48) <= element <= chr(57):
        digit_list.append(element)
    else:
        symbol_list.append(element)
for i in range(len(digit_list)):
    if i % 2 == 0:
        take_list.append(digit_list[i])
    else:
        skip_list.append(digit_list[i])
start = 0
end = 0
for i in range(len(take_list)):
    end += int(take_list[i])
    hidden_message += symbol_list[start:end]
    start += int(skip_list[i]) + int(take_list[i])
    end += int(skip_list[i])
print(''.join(hidden_message))