from collections import deque

sequence_numbers = input().split()
target_number = int(input())

pairs = set()
iterations = 0
numbers = deque([int(num) for num in sequence_numbers])

while numbers:
    first_num = numbers.popleft()
    for second_num in numbers:
        iterations += 1
        if first_num + second_num == target_number:
            current_pair = (first_num, second_num)
            pairs.add(current_pair)
            print(f"{first_num} + {second_num} = {target_number}")

print(f"Iterations done: {iterations}")
for pair in pairs:
    print(pair)