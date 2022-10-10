from collections import deque


def create_words_dict():
    words_to_find = ["rose", "tulip", "lotus", "daffodil"]
    words_dict = {}
    for current_word in words_to_find:
        words_dict[current_word] = []
        for _ in range(len(current_word)):
            words_dict[current_word].append("")
    return words_dict


def match_chr_in_word(word_char, words_dict):
    for word, letters in words_dict.items():
        for index, symbol in enumerate(word):
            if symbol == word_char and letters[index] == "":
                words_dict[word][index] = word_char
        if word == ''.join(letters):
            print(f"Word found: {word}")
            return True
    return False


vowels = deque(input().split())   # гласни
consonants = input().split()   # съгласни
words = create_words_dict()

is_found = False
while True:
    if not vowels or not consonants:
        break

    first_char = vowels.popleft()
    second_char = consonants.pop()

    if match_chr_in_word(first_char, words) or match_chr_in_word(second_char, words):
        is_found = True
        break

if not is_found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")