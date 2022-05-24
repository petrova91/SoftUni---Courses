film_name = input()
count_student_ticket = 0
count_standard_ticket = 0
count_kid_ticket = 0
count_busy_places = 0
while film_name != 'Finish':
    free_places = int(input())
    total_places = free_places
    count_sold_ticket = 0
    type_ticket = input()
    while type_ticket != 'End':
        if type_ticket == 'student':
            count_student_ticket += 1
            count_busy_places += 1
            free_places -= 1
            count_sold_ticket += 1
        elif type_ticket == 'standard':
            count_standard_ticket += 1
            count_busy_places += 1
            free_places -= 1
            count_sold_ticket += 1
        elif type_ticket == 'kid':
            count_kid_ticket += 1
            count_busy_places += 1
            free_places -= 1
            count_sold_ticket += 1
        if free_places == 0:
            break
        type_ticket = input()
    percent_busy_hall = (count_sold_ticket / total_places) * 100
    print(f'{film_name} - {percent_busy_hall:.2f}% full.')
    film_name = input()
percent_student_tickets = (count_student_ticket / count_busy_places) * 100
percent_standard_tickets = (count_standard_ticket / count_busy_places) * 100
percent_kid_tickets = (count_kid_ticket / count_busy_places) * 100
print(f'Total tickets: {count_busy_places}')
print(f'{percent_student_tickets:.2f}% student tickets.')
print(f'{percent_standard_tickets:.2f}% standard tickets.')
print(f'{percent_kid_tickets:.2f}% kids tickets.')