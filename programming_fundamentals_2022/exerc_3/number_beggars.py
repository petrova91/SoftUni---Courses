numbers = input()
count_beggars = int(input())
numbers = list(map(int, numbers.split(', ')))
index_of_beggar = 0
sum_beggar = []
while index_of_beggar < count_beggars:
    sum_current_beggar = 0
    for element in range(index_of_beggar, len(numbers), count_beggars):
        sum_current_beggar += numbers[element]
    sum_beggar.append(sum_current_beggar)
    index_of_beggar += 1
print(sum_beggar)
