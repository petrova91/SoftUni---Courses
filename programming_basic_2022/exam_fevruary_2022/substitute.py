number_k = int(input())
number_l = int(input())
number_m = int(input())
number_n = int(input())
count_substitute = 0
substitute_are_finish = False
for first_figure_first_number in range(number_k, 8+1):
    if first_figure_first_number % 2 == 0:
        for second_figure_first_number in range(9, number_l-1, -2):
            for first_figure_second_number in range(number_m, 8+1):
                if first_figure_second_number % 2 == 0:
                    for second_figure_second_number in range(9, number_n-1, -2):
                        if first_figure_first_number == first_figure_second_number and \
                            second_figure_first_number == second_figure_second_number:
                            print('Cannot change the same player.')
                        else:
                            count_substitute +=1
                            print(f'{first_figure_first_number}{second_figure_first_number} - {first_figure_second_number}{second_figure_second_number}')
                        if count_substitute == 6:
                            substitute_are_finish = True
                            break
                if substitute_are_finish:
                    break
            if substitute_are_finish:
                break
    if substitute_are_finish:
        break

