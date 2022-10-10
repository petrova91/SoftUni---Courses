import re


def read_searched_words(file_path):
    searched_words = []
    with open("words.txt") as file_path:
        searched_words = file_path.read().split()
    return searched_words


def calculate_words_count(file_path, searched_words):
    words_count = {}
    with open("text.txt") as file_path:
        text = file_path.read()
        for word in searched_words:
            pattern = fr"\b{word}\b"
            count = len(re.findall(pattern, text, re.IGNORECASE))
            words_count[word] = count
    return words_count


def print_result(file_path, words_count):
    with open("output.txt", "w") as file_path:
        for key, value in sorted(words_count.items(), key=lambda x: -x[1]):
            file_path.writelines(f"{key} - {value}\n")


words = read_searched_words("words.txt")
result = calculate_words_count("text.txt", words)
print_result("output.txt", result)
