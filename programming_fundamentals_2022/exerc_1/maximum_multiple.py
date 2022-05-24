divisor = int(input())   # делител
boundary = int(input())   # граница
largest_number = 1
for current_number in range(1, boundary +1):
    if current_number % divisor == 0:
        if current_number > largest_number:
            largest_number = current_number
print(largest_number)
