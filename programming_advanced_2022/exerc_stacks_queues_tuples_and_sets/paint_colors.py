from collections import deque

text = deque(input().split())

collected_colors = []
main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

while text:
    first_part = text.popleft()
    if not text:
        second_part = ""
    else:
        second_part = text.pop()
    first_combination = first_part + second_part
    second_combination = second_part + first_part
    if first_combination in main_colors or first_combination in secondary_colors:
        collected_colors.append(first_combination)
    elif second_combination in main_colors or second_combination in secondary_colors:
        collected_colors.append(second_combination)
    else:
        first_part = first_part[:-1]
        second_part = second_part[:-1]
        if first_part:
            middle = len(text) // 2
            text.insert(middle, first_part)
        if second_part:
            middle = len(text) // 2
            text.insert(middle, second_part)

result = []
for color in collected_colors:
    if color in secondary_colors:
        if secondary_colors[color].issubset(collected_colors):
            result.append(color)
    else:
        result.append(color)

print(result)