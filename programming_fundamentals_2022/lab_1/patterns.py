# number = int(input())
# for column in range(1, number+1):
#     for row in range(1, column+1):
#         print('*', end='')
#     print()
# for column in range(number-1, 0, -1):
#     for row in range(column, 0, -1):
#         print('*', end='')
#     print()

number = int(input())
for i in range(1, number+1):
    print(i * '*')
for j in range(number-1, 0, -1):
    print(j * '*')