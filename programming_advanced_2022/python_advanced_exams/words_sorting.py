def get_sum_of_letters(word):
    total_sum = 0
    for letter in word:
        total_sum += ord(letter)
    return total_sum


def words_sorting(*args):
    words = {}
    result = ""
    for word in args:
        words[word] = get_sum_of_letters(word)
    total_sum = sum(words.values())
    sort_words = ""
    if total_sum % 2 == 0:
        sort_words = sorted(words.items(), key=lambda x: x[0])
    else:
        sort_words = sorted(words.items(), key=lambda x: -x[1])

    for key, value in sort_words:
        result += f"{key} - {value}" + "\n"
    return result


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))



