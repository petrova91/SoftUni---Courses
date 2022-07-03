numbers = input().split()
absolute_values = []
for digit in numbers:
    absolute_values.append(abs(float(digit)))
print(absolute_values)