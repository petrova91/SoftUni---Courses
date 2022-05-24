count_judge = int(input())
name_presentation = input()
total_count_score = 0
count_score = 0
while name_presentation != 'Finish':
    counter_current_score = 0
    current_average_score = 0
    for current_score in range(1, count_judge + 1):
        score = float(input())
        counter_current_score += score
        total_count_score += score
        count_score += 1
        current_average_score = counter_current_score / count_judge
    print(f'{name_presentation} - {current_average_score:.2f}.')
    name_presentation = input()
total_average_score = total_count_score / count_score
print(f"Student's final assessment is {total_average_score:.2f}.")