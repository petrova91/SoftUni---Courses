symbols = {"-", ",", ".", "!", "?"}

with open("./text_01.txt") as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            result = " ".join(line.strip().split()[::-1])
            for symbol in symbols:
                result = result.replace(symbol, "@")
            print(result)
