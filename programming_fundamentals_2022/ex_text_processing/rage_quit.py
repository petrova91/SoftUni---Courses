some_text = input().upper()
sequence_of_symbols = ""
result = ""
number = ""
for index, symbol in enumerate(some_text):
    if symbol.isdigit():
        number += symbol
        if index <= len(some_text)-2 and some_text[index+1].isdigit():
            continue
        result += sequence_of_symbols * int(number)
        sequence_of_symbols = ""
        number = ""
    else:
        sequence_of_symbols += symbol
print(f"Unique symbols used: {len(set(result))}")
print(result)