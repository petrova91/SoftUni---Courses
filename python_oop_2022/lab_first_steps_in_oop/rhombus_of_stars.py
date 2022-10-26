def print_rhombus(row, n):
    for space in range(n - row):
        print(" ", end="")
    for star in range(row - 1):
        print("*", end=" ")
    print("*")


def create_upper_part(n):
    for row in range(1, n + 1):
        print_rhombus(row, n)


def create_button_part(n):
    for row in range(n - 1, 0, -1):
        print_rhombus(row, n)


def create_rhombus():
    create_upper_part(size)
    create_button_part(size)


size = int(input())
create_rhombus()
