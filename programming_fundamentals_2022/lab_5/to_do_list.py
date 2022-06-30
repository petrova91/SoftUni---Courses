command = input().split('-')
sorted_list = [''] * 10
task_list = []
while 'End' not in command:
    index_importance = int(command[0]) - 1
    note = command[1]
    sorted_list.pop(index_importance)
    sorted_list.insert(index_importance, note)
    command = input().split('-')
task_list = [element for element in sorted_list if element != '']
print(task_list)