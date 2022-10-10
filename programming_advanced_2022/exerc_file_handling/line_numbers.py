from string import punctuation


def find_count_symbols(current_line):
    count_letters = 0
    count_punctuation = 0
    punctuation_symbols = list(punctuation)
    for el in current_line:
        if el.isalpha():
            count_letters += 1
        elif el in punctuation_symbols:
            count_punctuation += 1
    return count_letters, count_punctuation


with open("./text_02.txt") as input_file, open("./output.txt", "w") as output_file:
    for index, line in enumerate(input_file):
        letters, symbols = find_count_symbols(line)
        output_file.write(f"Line {index + 1}: {line.strip()} ({letters})({symbols})\n")
