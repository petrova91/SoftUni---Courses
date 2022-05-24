count_men = int(input())
count_women = int(input())
max_count_tables = int(input())
current_table = 1
for current_man in range(1, count_men + 1):
    for current_woman in range(1, count_women + 1):
        if current_table <= max_count_tables:
            print(f'({current_man} <-> {current_woman})', end=' ')
            current_table += 1

