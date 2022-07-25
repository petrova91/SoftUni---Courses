text = input().split()
total_result = 0
for element in text:
    result = 0
    number = int(element[1:len(element)-1])
    if element[0].isupper():
        result += number / (ord(element[0]) - 64)
    elif element[0].islower():
        result += number * (ord(element[0]) - 96)
    if element[-1].isupper():
        result -= (ord(element[-1]) - 64)
    elif element[-1].islower():
        result += (ord(element[-1]) - 96)
    total_result += result
print(f"{total_result:.2f}")
