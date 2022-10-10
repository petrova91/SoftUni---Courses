from collections import deque

seats = input().split(", ")
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])
rotations = 0
seat_matches = []

while True:
    if rotations == 10 or len(seat_matches) == 3:
        break

    rotations += 1
    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()

    ascii_char = chr(first_num + second_num)
    first_combination = str(first_num) + ascii_char
    second_combination = str(second_num) + ascii_char
    if first_combination in seats:
        seat_matches.append(first_combination)
        seats.remove(first_combination)
    elif second_combination in seats:
        seat_matches.append(second_combination)
        seats.remove(second_combination)
    else:
        first_sequence.append(first_num)
        second_sequence.appendleft(second_num)

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")
