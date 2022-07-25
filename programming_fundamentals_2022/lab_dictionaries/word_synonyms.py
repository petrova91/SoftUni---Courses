count_words = int(input())
synonyms_dict = {}
for i in range(count_words):
    word = input()
    synonym = input()
    if word not in synonyms_dict:
        synonyms_dict[word] = []
    synonyms_dict[word].append(synonym)
for key, value in synonyms_dict.items():
    print(f"{key} - {', '.join(value)}")