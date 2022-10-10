text = [elem for elem in input()]

symbols = {}

for letter in text:
    if letter not in symbols:
        symbols[letter] = 0
    symbols[letter] += 1

for data in sorted(symbols.items()):
    print(f"{data[0]}: {data[1]} time/s")
