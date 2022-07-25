start = input()
end = input()
sequence_letters = input()
total_sum = 0
for letter in sequence_letters:
    if ord(start) < ord(letter) < ord(end):
        total_sum += ord(letter)
print(total_sum)