def merge_command(command_line, text):
    start_index = int(command_line[1])
    end_index = int(command_line[2])
    if start_index < 0:
        start_index = 0
    if end_index >= len(text):
        end_index = len(text) - 1
    words_to_merge = text[start_index:end_index+1]
    merged_string = [''.join(words_to_merge)]
    new_text = text[:start_index] + merged_string + text[end_index + 1:]
    return new_text


def divide_command(command_line, text):
    index = int(command_line[1])
    partitions = int(command_line[2])
    if partitions == 0:
        partitions = 1
    word_to_divide = text[index]
    new_word = []
    count_element = len(word_to_divide) // partitions
    start_index = 0
    end_index = count_element
    for current_partition in range(partitions-1):
        parts = word_to_divide[start_index:end_index]
        new_word.append(parts)
        start_index += count_element
        end_index += count_element
    last_part = ''.join(word_to_divide[start_index:])
    new_word.append(last_part)
    new_part = [element for element in new_word]
    text = text[:index] + new_part + text[index+1:]
    # text[index] = ' '.join(new_word)
    return text


some_text = input().split()
command = input()
while command != '3:1':
    current_command = command.split()
    command_name = current_command[0]
    if command_name == 'merge':
        some_text = merge_command(current_command, some_text)
    elif command_name == 'divide':
        some_text = divide_command(current_command, some_text)
    command = input()
print(' '.join(some_text))