some_string = input()
strength_explosion = 0
left_symbols = ""
for symbol in some_string:
    if symbol == ">":
        left_symbols += symbol
    elif symbol.isdigit():
        strength_explosion += int(symbol)
        strength_explosion -= 1
    elif symbol.isalpha():
        if strength_explosion == 0:
            left_symbols += symbol
        else:
            strength_explosion -= 1
print(left_symbols)
