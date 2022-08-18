words = input().split(" | ")
dictionary = {}
for current_word in words:
    word, definition = current_word.split(": ")
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(definition)
test_words = input().split(" | ")
command = input()
if command == "Test":
    for test_word in test_words:
        if test_word in dictionary:
            print(f"{test_word}:")
            sep = "\n-"
            print(f'-{sep.join(dictionary[test_word])}')
elif command == "Hand Over":
    for my_word in dictionary:
        print(f"{my_word}", end=" ")
