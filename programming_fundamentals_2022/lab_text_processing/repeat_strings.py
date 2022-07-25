sequence_of_string = input().split()
repeat_string = ""
for element in sequence_of_string:
    repeat_string += element * len(element)
print(repeat_string)