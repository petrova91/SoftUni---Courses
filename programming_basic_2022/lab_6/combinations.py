number = int(input())
counter = 0
for first_number in range(0, number + 1):
    for second_number in range(0, number + 1):
        for third_number in range(0, number + 1):
            sum = first_number + second_number + third_number
            if sum == number:
                counter += 1
print(counter)