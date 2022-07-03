number = int(input())
prime_number = True
for digit in range(2, number):
    if number % digit == 0:
        prime_number = False
        break
print(prime_number)

