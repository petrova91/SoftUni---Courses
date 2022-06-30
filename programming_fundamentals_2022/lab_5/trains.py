numbers_wagons = int(input())
train = [0] * numbers_wagons
command = input().split()
while 'End' not in command:
    command_name = command[0]
    count_people = int(command[-1])
    if command_name == 'add':
        train[-1] += count_people
    elif command_name == 'insert':
        index = int(command[1])
        train[index] += count_people
    elif command_name == 'leave':
        index = int(command[1])
        train[index] -= count_people
    command = input().split()
print(train)
