import math

word = input()
powerful_word = ''
power_of_word = 0
while word != 'End of words':
    sum = 0
    for index in range(len(word)):
        number_of_index = ord(word[index])
        sum += number_of_index
    word_lower_case = word.casefold()  # функцията прави главните букви малки
    if word_lower_case[0] == 'a' or word_lower_case[0] == 'e' or word_lower_case[0] == 'i' or\
            word_lower_case[0] == 'o' or word_lower_case[0] == 'u' or word_lower_case[0] == 'y':
        sum *= len(word)
    else:
        sum /= len(word)
        sum = math.floor(sum)
    if power_of_word < sum:
        power_of_word = sum
        powerful_word = word
    word = input()
print(f'The most powerful word is {powerful_word} - {power_of_word}')