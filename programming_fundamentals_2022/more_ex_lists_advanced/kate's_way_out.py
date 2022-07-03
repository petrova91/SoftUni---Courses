count_rows = int(input())
maze = []
count_moves = 0
for row in range(count_rows):
    current_row = input()
    maze_row = [letter for letter in current_row]
    maze.append(maze_row)
for current_list in maze:
    if 'k' in current_list:
        kate_index = current_list.index('k')
        print(kate_index)